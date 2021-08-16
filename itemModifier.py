from enum import Enum

from attr import attrs

class ItemModifierType(Enum):
    PSEUDO = "pseudo"
    EXPLICIT = "explicit"
    IMPLICIT = "implicit"
    FRACTURED = "fractured"
    ENCHANT = "enchant"
    CRAFTED = "crafted"
    VEILED = "veiled"
    MONSTER = "monster"
    DELVE = "delve"
    ULTIMATUM = 'ultimatum'


@attrs(auto_attribs=True, frozen=True)
class ItemModifier:
    type: ItemModifierType
    id: str
    text: str
    classid :str
    options: dict

