import importlib
import inspect
import os
import traceback
from copy import deepcopy
from datetime import datetime
from pathlib import Path

import yaml

from generation.objects.player_generator import PlayerGenerator
from model.game.state.game_state import GameState
from validation.formal.base.abstract_validation import AbstractValidation


class FormalQuestValidator:
    RESULTS_ROOT = Path("results") / "validation"
    PASS_EMOJI = "✅"
    FAIL_EMOJI = "❌"
    ERROR_EMOJI = "⚠️"

    def __init__(self, quest_dirs: list[str], context: GameState):
        self.quest_dirs = [Path(quest_dir) for quest_dir in quest_dirs]
        self.context = context
        self.base_validations = [
            "validation.formal.entities_existence.EntitiesExistenceValidation",
            "validation.formal.all_quest_keys_exist.AllQuestKeysExistValidation",
            "validation.formal.enemy.balance.BalanceValidation",
        ]

    @staticmethod
    def find_content_files(experiment_dir: str) -> list[str]:
        root = Path(experiment_dir)
        if not root.exists():
            return []

        dirs = {
            str(content_file.parent)
            for content_file in root.rglob("content.yaml")
            if content_file.is_file()
        }
        return sorted(dirs)

    def validate(self, experiment_dir: str | None = None):
        if experiment_dir is not None:
            self.base_dir = Path(experiment_dir)
            self.quest_dirs = [Path(quest_dir) for quest_dir in self.find_content_files(experiment_dir)]

        if not self.quest_dirs:
            return {}

        if self.base_dir is None:
            self.base_dir = self._infer_base_dir()

        validation_modules = self._collect_validation_modules()
        grouped_results = {}

        for quest_dir in sorted(self.quest_dirs):
            quest_result = self._validate_quest(quest_dir, validation_modules)
            group_key, quest_label = self._get_group_and_quest_label(quest_dir)

            grouped_results.setdefault(group_key, []).append((quest_label, quest_dir, quest_result))
            self._write_quest_result(quest_dir, group_key, quest_result)

        for group_key, quest_items in grouped_results.items():
            self._write_summary(group_key, quest_items)

        return grouped_results

    def _collect_validation_modules(self) -> list[str]:
        discovered_modules = []
        validation_root = Path("validation") / "formal"

        for py_file in validation_root.rglob("*.py"):
            if py_file.name == "__init__.py":
                continue
            if py_file.parts[-2:] == ("base", "abstract_validation.py"):
                continue

            module_path = ".".join(py_file.with_suffix("").parts)
            discovered_modules.append(module_path)

        ordered_modules = []
        seen = set()

        for module_path in self.base_validations:
            if module_path not in seen:
                ordered_modules.append(module_path)
                seen.add(module_path)

        for module_path in sorted(discovered_modules):
            if module_path not in seen:
                ordered_modules.append(module_path)
                seen.add(module_path)

        return ordered_modules

    def _infer_base_dir(self) -> Path:
        common_path = os.path.commonpath([str(quest_dir) for quest_dir in self.quest_dirs])
        return Path(common_path).parent

    def _get_group_and_quest_label(self, quest_dir: Path) -> tuple[str, str]:
        try:
            relative = quest_dir.relative_to(self.base_dir)
        except ValueError:
            return quest_dir.parent.name, quest_dir.name

        if not relative.parts:
            return quest_dir.parent.name, quest_dir.name

        group_key = relative.parts[0]
        quest_label_parts = relative.parts[1:]
        quest_label = "/".join(quest_label_parts) if quest_label_parts else relative.name
        return group_key, quest_label

    def _validate_quest(self, quest_dir: Path, validation_modules: list[str]) -> list[dict]:
        content_file = quest_dir / "content.yaml"
        load_error_traceback = None

        try:
            quest = self._load_quest(content_file)
        except Exception:
            quest = None
            load_error_traceback = traceback.format_exc()

        results = []
        for module_path in validation_modules:
            results.append(self._run_validation(module_path, quest, load_error_traceback))

        return results

    def _load_quest(self, content_file: Path) -> dict:
        with content_file.open("r", encoding="utf-8") as file:
            raw_content = yaml.safe_load(file)

        if raw_content is None:
            raise ValueError(f"Файл пустой: {content_file}")

        if isinstance(raw_content, dict) and isinstance(raw_content.get("quest"), dict):
            return raw_content["quest"]

        if isinstance(raw_content, dict):
            return raw_content

        raise ValueError(f"Корень YAML должен быть словарём: {content_file}")

    def _run_validation(self, module_path: str, quest: dict | None, load_error_traceback: str | None) -> dict:
        validation_name = module_path.rsplit(".", 1)[-1]

        try:
            validation_class = self._load_validation_class(module_path)
            validation = self._instantiate_validation(validation_class)
            description = getattr(validation, "description", getattr(validation_class, "description", ""))

            if load_error_traceback is not None:
                return self._build_result(validation_name, description, "error", error_traceback=load_error_traceback)

            is_valid = bool(validation.validate(quest))
            status = "passed" if is_valid else "failed"
            return self._build_result(validation_name, description, status)
        except Exception:
            return self._build_result(
                validation_name,
                "Не удалось выполнить валидацию",
                "error",
                error_traceback=traceback.format_exc(),
            )

    def _load_validation_class(self, module_path: str):
        module = importlib.import_module(module_path)

        validation_classes = []
        for _, obj in inspect.getmembers(module, inspect.isclass):
            if obj.__module__ != module.__name__:
                continue
            if obj is AbstractValidation:
                continue
            if not issubclass(obj, AbstractValidation):
                continue
            if inspect.isabstract(obj):
                continue
            validation_classes.append(obj)

        if not validation_classes:
            raise ValueError(f"В модуле не найдена валидация: {module_path}")

        return validation_classes[0]

    def _instantiate_validation(self, validation_class):
        signature = inspect.signature(validation_class)
        required_params = [
            parameter
            for parameter in signature.parameters.values()
            if parameter.default is inspect._empty
            and parameter.kind in (inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.POSITIONAL_OR_KEYWORD)
        ]

        if not required_params:
            return validation_class()

        return validation_class(deepcopy(self.player))

    def _build_result(
        self,
        validation_name: str,
        description: str,
        status: str,
        error_traceback: str | None = None,
    ) -> dict:
        return {
            "name": validation_name,
            "description": description,
            "status": status,
            "emoji": self._status_to_emoji(status),
            "traceback": error_traceback,
        }

    def _status_to_emoji(self, status: str) -> str:
        if status == "passed":
            return self.PASS_EMOJI
        if status == "failed":
            return self.FAIL_EMOJI
        return self.ERROR_EMOJI

        def _write_quest_result(self, quest_dir: Path, group_key: str, quest_result: list[dict]):
        relative_dir = self._quest_relative_directory(quest_dir)
        output_dir = self.RESULTS_ROOT / group_key / relative_dir
        output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / f"{quest_dir.name}_results.md"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        quest_header = quest_dir.as_posix().rstrip("/") + "/"
        lines = [
            f"# {quest_header}",
            timestamp,
            "",
        ]

        for item in quest_result:
            lines.append(f"**{item['name']}**")
            lines.append(f"{item['description']}: {item['emoji']}")
            if item["status"] == "error" and item.get("traceback"):
                lines.append("```text")
                lines.append(item["traceback"].rstrip())
                lines.append("```")
            lines.append("")

        output_file.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    def _write_summary(self, group_key: str, quest_items: list[tuple[str, Path, list[dict]]]):
        output_dir = self.RESULTS_ROOT / group_key
        output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / "summary.md"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        quest_items = sorted(quest_items, key=lambda item: item[0])
        quest_labels = [item[0] for item in quest_items]
        validation_count = len(quest_items[0][2]) if quest_items else 0
        group_path = self.base_dir / group_key if self.base_dir is not None else Path(group_key)
        group_header = group_path.as_posix().rstrip("/") + "/"

        lines = [
            f"# {group_header}",
            timestamp,
            "",
        ]

        header_cells = ["Валидация", *quest_labels]
        lines.append("| " + " | ".join(header_cells) + " |")
        lines.append("| " + " | ".join(["---"] * len(header_cells)) + " |")

        for index in range(validation_count):
            first_result = quest_items[0][2][index]
            validation_label = f"**{first_result['name']}**<br>{first_result['description']}"
            row_cells = [validation_label]
            for _, _, quest_result in quest_items:
                row_cells.append(quest_result[index]["emoji"])
            lines.append("| " + " | ".join(row_cells) + " |")

        for status_name, status_key in (("Пройдено", "passed"), ("Не пройдено", "failed"), ("Ошибка", "error")):
            row_cells = [status_name]
            for _, _, quest_result in quest_items:
                total = len(quest_result)
                count = sum(1 for item in quest_result if item["status"] == status_key)
                percent = (count / total * 100) if total else 0.0
                row_cells.append(f"{count}/{total} ({percent:.1f}%)")
            lines.append("| " + " | ".join(row_cells) + " |")

        output_file.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


    def _quest_relative_directory(self, quest_dir: Path) -> Path:
        try:
            relative = quest_dir.relative_to(self.base_dir)
        except ValueError:
            return Path()

        if len(relative.parts) <= 1:
            return Path()

        return Path(*relative.parts[1:-1])

