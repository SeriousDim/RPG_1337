from dataclasses import dataclass
from enum import Enum

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

    def validate(self, directory: str | Path, player: Any = None, interacted_character: Any = None):
        validation_results = []

        for subfolder_path in self.get_subfolder_paths(directory):
            content_yaml_path = subfolder_path / "content.yaml"
            if not content_yaml_path.exists():
                continue

            with content_yaml_path.open("r", encoding="utf-8") as file:
                quest_yaml = yaml.safe_load(file)

            validation_result = self.run_validations_for_yaml(
                quest_yaml,
                player=player,
                interacted_character=interacted_character,
            )
            validation_results.append(
                {
                    "path": content_yaml_path,
                    "quest": quest_yaml,
                    "result": validation_result,
                }
            )

        return validation_results

    def run_validations_for_yaml(self, quest_yaml: dict, player: Any, interacted_character: Any):
        base_validations = self.create_base_validations(player)
        other_validations = self.create_other_validations(player, interacted_character)

        base_results = self.run_validation_list(base_validations, quest_yaml)
        other_results = self.run_validation_list(other_validations, quest_yaml)

        return {
            "base_validations": [result.to_dict() for result in base_results],
            "other_validations": [result.to_dict() for result in other_results],
        }

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
