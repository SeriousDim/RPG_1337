import json
from pathlib import Path

from experiment.formal_validator import (
    VALIDATION_EMOJI_BY_STATUS,
    ValidationResult,
    ValidationStatus,
)



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

    def generate_summary(self, directory: str | Path) -> None:
        base_path = Path(directory)
        subfolder_paths = self.get_subfolder_paths(base_path)

        validation_results_groups: list[tuple[str, list[ValidationResult]]] = []
        for subfolder_path in subfolder_paths:
            json_files = sorted(subfolder_path.glob("*.json"))
            if not json_files:
                continue

            validation_results_groups.append(
                (subfolder_path.name, self._load_validation_results_from_json(json_files[0]))
            )

        summary_markdown = self.generate(validation_results_groups)
        self.save_summary(base_path, summary_markdown)



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

    def generate(self, validation_results_groups: list[tuple[str, list[ValidationResult]]]) -> str:
        if not validation_results_groups:
            return "|   | Успешно | Провал | Ошибка |\n| --- | --- | --- | --- |\n"

        folder_names = [folder_name for folder_name, _ in validation_results_groups]
        validation_names: list[str] = []
        seen_validation_names: set[str] = set()
        results_by_folder: list[dict[str, ValidationResult]] = []

        for _, validation_results in validation_results_groups:
            folder_results: dict[str, ValidationResult] = {}
            for validation_result in validation_results:
                folder_results[validation_result.validation] = validation_result
                if validation_result.validation not in seen_validation_names:
                    seen_validation_names.add(validation_result.validation)
                    validation_names.append(validation_result.validation)
            results_by_folder.append(folder_results)

        lines = [
            "|   | " + " | ".join(folder_names) + " | Успешно | Провал | Ошибка |",
            "| --- | " + " | ".join(["---"] * len(folder_names)) + " | --- | --- | --- |",
        ]

        for validation_name in validation_names:
            row_cells = [validation_name]
            success_count = 0
            failure_count = 0
            error_count = 0

            for folder_results in results_by_folder:
                validation_result = folder_results.get(validation_name)
                if validation_result is None:
                    row_cells.append("")
                    continue

                row_cells.append(VALIDATION_EMOJI_BY_STATUS[validation_result.result])
                if validation_result.result == ValidationStatus.SUCCESS:
                    success_count += 1
                elif validation_result.result == ValidationStatus.FAILURE:
                    failure_count += 1
                else:
                    error_count += 1

            total_folders = len(folder_names)
            row_cells.extend(
                [
                    self._format_ratio(success_count, total_folders),
                    self._format_ratio(failure_count, total_folders),
                    self._format_ratio(error_count, total_folders),
                ]
            )
            lines.append("| " + " | ".join(row_cells) + " |")

        validation_status_rows = [
            ("Пройдено", ValidationStatus.SUCCESS),
            ("Не пройдено", ValidationStatus.FAILURE),
            ("Ошибка", ValidationStatus.ERROR),
        ]

        for row_title, status in validation_status_rows:
            row_cells = [row_title]
            for folder_results in results_by_folder:
                folder_total = len(folder_results)
                status_count = sum(1 for result in folder_results.values() if result.result == status)
                row_cells.append(self._format_ratio(status_count, folder_total))

            row_cells.extend(["", "", ""])
            lines.append("| " + " | ".join(row_cells) + " |")

        return "\n".join(lines) + "\n"

    def save_summary(self, directory: str | Path, summary_markdown: str) -> Path:
        base_path = Path(directory)
        summary_path = base_path / "summary.md"
        summary_path.parent.mkdir(parents=True, exist_ok=True)
        summary_path.write_text(summary_markdown, encoding="utf-8")
        return summary_path

    def _format_ratio(self, value: int, total: int) -> str:
        if total == 0:
            return "0/0 (0%)"

        percent = value / total * 100
        if float(percent).is_integer():
            percent_text = f"{int(percent)}%"
        else:
            percent_text = f"{percent:.1f}%"

        return f"{value}/{total} ({percent_text})"



