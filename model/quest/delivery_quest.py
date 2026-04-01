from dataclasses import dataclass

from model.items.resource import Resource
from model.mobs.character import Character
from model.mobs.enemy import Enemy
from model.quest.dialogs import DialogsPart
from model.quest.quest import Quest

@dataclass
class ResourceToDeliver(DialogsPart):
    resource: Resource
    amount: int


@dataclass
class EnemyToFace(DialogsPart):
    enemy: Enemy
    enemy_amount: int


@dataclass
class Destination(DialogsPart):
    character_to_deliver: Character


@dataclass
class DeliveryQuestParts:
    resource_to_deliver: ResourceToDeliver
    enemy_to_face: EnemyToFace
    destination: Destination


@dataclass
class DeliveryQuest(Quest):
    parts: DeliveryQuestParts
    objective_description: str
