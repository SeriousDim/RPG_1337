import json
from pathlib import Path

from experiment.formal_validator import ValidationResult, ValidationStatus


class ValidationSummary:
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

    def generate_summary(self, directory: str | Path):
        base_path = Path(directory)
        subfolder_paths = self.get_subfolder_paths(base_path)

        validation_results_groups: list[list[ValidationResult]] = []
        for subfolder_path in subfolder_paths:
            json_files = sorted(subfolder_path.glob("*.json"))
            if not json_files:
                continue

            validation_results_groups.append(self._load_validation_results_from_json(json_files[0]))

        self.generate(validation_results_groups)

    def _load_validation_results_from_json(self, json_path: Path) -> list[ValidationResult]:
        data = json.loads(json_path.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            raise ValueError(f"Validation JSON must contain a list: {json_path}")

        validation_results: list[ValidationResult] = []
        for item in data:
            if not isinstance(item, dict):
                raise ValueError(f"Each validation item must be an object: {json_path}")

            validation_results.append(
                ValidationResult(
                    validation=item.get("validation", ""),
                    description=item.get("description", ""),
                    result=ValidationStatus(item["result"]),
                    error=item.get("error"),
                )
            )

        return validation_results

    def generate(self, validation_results_groups: list[list[ValidationResult]]) -> None:
        pass

