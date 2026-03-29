from __future__ import annotations

from pathlib import Path


class ResourceLoader:
    RESOURCES_DIR: Path = Path("resources")

    @staticmethod
    def _safe_resolve(filename: str) -> Path:
        base = ResourceLoader.RESOURCES_DIR.resolve()
        path = (base / filename).resolve()

        if path != base and base not in path.parents:
            raise ValueError(f"Недопустимый путь: {filename!r}")

        return path

    @staticmethod
    def load_bytes(filename: str) -> bytes:
        path = ResourceLoader._safe_resolve(filename)
        if not path.is_file():
            raise FileNotFoundError(f"Файл не найден: {path}")
        return path.read_bytes()

    @staticmethod
    def load_text(filename: str, encoding: str = "utf-8") -> str:
        path = ResourceLoader._safe_resolve(filename)
        if not path.is_file():
            raise FileNotFoundError(f"Файл не найден: {path}")
        return path.read_text(encoding=encoding)
