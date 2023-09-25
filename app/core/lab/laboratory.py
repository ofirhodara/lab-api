from typing import List, Dict, Generic
from pydantic import BaseModel

from app.core.lab.items import Port, Card, Component
from result import Ok, Err

from app.managers.logger_manager import create_logger

logger = create_logger(__name__)


class Laboratory(BaseModel):
    _laboratory_class_mapper: Dict[str, BaseModel] = {
        "Component": Component,
        "Card": Card,
        "Port": Port
    }
    component: List[Component]
    cards: List[Card]
    ports: List[Port]

    @staticmethod
    def get_lab_class_by_name(class_name: str) -> Generic:
        if class_name in Laboratory._laboratory_class_mapper.keys():
            return Ok(Laboratory._laboratory_class_mapper[class_name])
        e_message = f"The class {class_name} is not one of our Laboratory items classes"
        logger.fatal(e_message)
        return Err(e_message)
