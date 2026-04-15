"""Utilities for reading the prompt and generated quest files."""

from __future__ import annotations

from pathlib import Path


PROMPT_PATH = Path(__file__).resolve().parent / "resources" / "prompts" / "automata_v2_delivery_v2.txt"


def read_prompt_and_generated_quest(quest_path: str | Path) -> tuple[str, str]:
    """Read the fixed prompt and a generated quest from disk.

    Args:
        quest_path: Path to the generated quest file.

    Returns:
        A tuple of (prompt_text, generated_quest_text).
    """
    prompt_text = PROMPT_PATH.read_text(encoding="utf-8")
    generated_quest_text = Path(quest_path).read_text(encoding="utf-8")
    return prompt_text, generated_quest_text

