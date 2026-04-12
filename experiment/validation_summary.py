from pathlib import Path


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
    
    def generate_summary(self, ):
