from dataclasses import field
from marshmallow_dataclass import dataclass


from pet_properties import PetProperties


@dataclass
class Pet(PetProperties):
    id: int = field(
        metadata={"description": "Unique identifier for the Pet", "required": True}
    )
