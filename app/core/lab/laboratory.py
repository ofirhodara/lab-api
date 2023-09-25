from typing import List

from pydantic import BaseModel

from app.core.lab.items import Port, Card, Component


class Laboratory(BaseModel):
    Component: List[Component]
    cards: List[Card]
    ports: List[Port]

