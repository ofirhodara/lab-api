import uuid
from app.core.lab.items_details import ItemConnection, ItemState, ItemQuality

from pydantic import BaseModel


class Card(BaseModel):
    component_id: uuid.UUID
    index: int
    card_type: ItemQuality


class Port(BaseModel):
    component_id: uuid.UUID
    state: ItemConnection  # is connected?
    index: int
    card_index: int


class Component(BaseModel):
    comp_id: uuid.UUID
    version: int
    state: ItemState
    card_index: int
