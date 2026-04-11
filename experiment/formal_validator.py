from dataclasses import dataclass
from datetime import datetime
from enum import Enum
import json
from pathlib import Path
from typing import Any
import traceback

import yaml


from validation.formal.base.abstract_validation import AbstractValidation

from validation.formal.all_quest_keys_exist import AllQuestKeysExistValidation
from validation.formal.delivery.characters_in_different_locations import CharactersInDifferentLocationsValidation
from validation.formal.delivery.item_is_acceptable_by_character import ItemIsAcceptableByCharacterValidation
from validation.formal.delivery.player_has_appropriate_instrument import PlayerHasAppropriateInstrumentValidation
from validation.formal.dialogs.character_is_same_player_interacted import CharacterIsSamePlayerInteractedValidation
from validation.formal.dialogs.remark import RemarkValidation
from validation.formal.enemy.balance import BalanceValidation
from validation.formal.entities_existence import EntitiesExistenceValidation
from validation.formal.reward.character_can_give_reward import CharacterCanGiveRewardValidation
from validation.formal.reward.player_has_not_such_reward import PlayerHasNotSuchRewardValidation
from validation.formal.reward.reward_is_better_than_players_one import RewardIsBetterThanPlayersOneValidation


class ValidationStatus(str, Enum):
    SUCCESS = "успешно"
    FAILURE = "провал"
    ERROR = "ошибка"


VALIDATION_EMOJI_BY_STATUS = {
    ValidationStatus.SUCCESS: "✅",
    ValidationStatus.FAILURE: "❌",
    ValidationStatus.ERROR: "⚠️",
}



@dataclass(slots=True)
class ValidationResult:
    validation: str
    description: str
    result: ValidationStatus
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "validation": self.validation,
            "description": self.description,
            "result": self.result.value,
            "error": self.error,
        }


class FormalQuestValidator:
    def get_subfolder_paths(self, directory: str | Path) -> list[Path]:
        """Возвращает список путей ко всем подпапкам внутри указанной директории."""
        base_path = Path(directory)

        if not base_path.exists():
            raise FileNotFoundError(f"Directory does not exist: {base_path}")

        if not base_path.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {base_path}")

        subfolder_paths: list[Path] = []
        for path in base_path.rglob("*"):
            if path.is_dir():
                subfolder_paths.append(path)

        return sorted(subfolder_paths)

    def validate(self, directory: str | Path, player: Any = None, interacted_character: Any = None) -> None:
        base_path = Path(directory)

        for subfolder_path in self.get_subfolder_paths(base_path):
            content_yaml_path = subfolder_path / "content.yaml"
            if not content_yaml_path.exists():
                continue

            with content_yaml_path.open("r", encoding="utf-8") as file:
                quest_yaml = yaml.safe_load(file)

            self.run_validations_for_yaml(
                quest_yaml,
                content_yaml_path=content_yaml_path,
                base_directory=base_path,
                player=player,
                interacted_character=interacted_character,
            )


    def run_validations_for_yaml(
        self,
        quest_yaml: dict,
        content_yaml_path: Path,
        base_directory: Path,
        player: Any,
        interacted_character: Any,
    ):
        base_validations = self.create_base_validations(player)
        other_validations = self.create_other_validations(player, interacted_character)
        base_results = self.run_validation_list(base_validations, quest_yaml)
        other_results = self.run_validation_list(other_validations, quest_yaml)
        all_results = base_results + other_results
        self.save_validation_artifacts(
            content_yaml_path=content_yaml_path,
            base_directory=base_directory,
            validation_results=all_results)


    def save_validation_artifacts(
        self,
        content_yaml_path: Path,
        base_directory: Path,
        validation_results: list[ValidationResult],
    ) -> None:
        relative_path = content_yaml_path.parent.relative_to(base_directory)
        parts = relative_path.parts

        experiment_name = parts[0] if len(parts) > 0 else content_yaml_path.parent.name
        subfolder_path = Path(*parts[1:]) if len(parts) > 1 else Path(content_yaml_path.parent.name)
        folder_path = content_yaml_path.parent.as_posix()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        report_dir = Path("results") / "validation" / experiment_name / "report"
        json_dir = Path("results") / "validation" / experiment_name / "json"
        report_dir.mkdir(parents=True, exist_ok=True)
        json_dir.mkdir(parents=True, exist_ok=True)

        report_path = report_dir / f"{subfolder_path.name}.md"
        json_path = json_dir / f"{subfolder_path.name}.json"

        report_content = self.build_markdown_report(
            folder_path=folder_path,
            timestamp=timestamp,
            validation_results=validation_results,
        )
        report_path.write_text(report_content, encoding="utf-8")
        json_path.write_text(
            json.dumps([result.to_dict() for result in validation_results], ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def build_markdown_report(
        self,
        folder_path: str,
        timestamp: str,
        validation_results: list[ValidationResult],
    ) -> str:
        lines = [f"# {folder_path}", timestamp, '']

        for validation_result in validation_results:
            emoji = VALIDATION_EMOJI_BY_STATUS[validation_result.result]
            lines.append(f"{validation_result.validation}: {emoji}")
            if validation_result.description:
                lines.append(validation_result.description)

            if validation_result.result == ValidationStatus.ERROR and validation_result.error:
                lines.append("")
                lines.append("```")
                lines.append(validation_result.error.rstrip())
                lines.append("```")

            lines.append("")

        return "\n".join(lines).rstrip() + "\n"


    def create_base_validations(self, player: Any) -> list[AbstractValidation]:
        return [
            AllQuestKeysExistValidation(),
            EntitiesExistenceValidation(),
            BalanceValidation(player),
        ]

    def create_other_validations(self, player: Any, interacted_character: Any) -> list[AbstractValidation]:
        return [
            PlayerHasAppropriateInstrumentValidation(player),
            RewardIsBetterThanPlayersOneValidation(player),
            PlayerHasNotSuchRewardValidation(player),
            CharacterIsSamePlayerInteractedValidation(interacted_character),
            CharactersInDifferentLocationsValidation(),
            ItemIsAcceptableByCharacterValidation(),
            CharacterCanGiveRewardValidation(),
            RemarkValidation(),
        ]

    def run_validation_list(self, validations: list[AbstractValidation], quest_yaml: dict) -> list[ValidationResult]:
        results: list[ValidationResult] = []

        for validation in validations:
            try:
                validation_result = validation.validate(quest_yaml)
                result = ValidationStatus.SUCCESS if validation_result else ValidationStatus.FAILURE
                error = None
            except Exception:
                result = ValidationStatus.ERROR
                error = traceback.format_exc()

            results.append(
                ValidationResult(
                    validation=validation.__class__.__name__,
                    description=getattr(validation, "description", ""),
                    result=result,
                    error=error,
                )
            )

        return results
