import ipaddress
import uuid

from pydantic import BaseModel, validator

from app.core.lab.items_details import ItemConnection, ItemState, ItemType


class LabDataItem(BaseModel):
    pass


class Card(LabDataItem):
    component_id: uuid.UUID = uuid.uuid1()
    index: int = 0
    card_type: ItemType = ItemType.GOOD


class Port(LabDataItem):
    component_id: uuid.UUID = uuid.uuid1()
    state: ItemConnection = ItemConnection.DISABLED
    index: int = 0
    card_index: int = 0


class Component(LabDataItem):
    comp_id: uuid.UUID = uuid.uuid1()
    version: int = 0
    state: ItemState = ItemState.OFF
    ip: str = "127.0.0.1"

    @validator("ip")
    def validate_ipv4(cls, value):
        try:
            # Attempt to parse the input value as an IPv4 address
            ip = ipaddress.IPv4Address(value)
        except ValueError:
            raise ValueError("Invalid IPv4 address format")
        return value
