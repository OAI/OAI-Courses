from dataclasses import field
from apiflask import Schema
from marshmallow_dataclass import dataclass


@dataclass
class PetProperties(Schema):
    """Attributes of a Pet that can be added to the Petstore"""

    name: str = field(metadata={"description": "Name of the pet", "required": True})
    tag: str = field(metadata={"description": "Pet category", "required": False})
