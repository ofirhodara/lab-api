from enum import Enum


class ItemState(Enum):
    OFF = "OFFLINE"
    ON = "ONLINE"


class ItemConnection(Enum):
    ENABLED = "connected"
    DISABLED = "disconnected"


class ItemType(Enum):
    GOOD = "GREAT_ONE"
    BAD = "WORST_ONE"
