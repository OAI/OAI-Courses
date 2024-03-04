from dataclasses import field
from apiflask import Schema, HTTPError
from marshmallow_dataclass import dataclass


@dataclass
class Error(Schema):
    code: int = field(
        metadata={"description": "Unique code for the error returned", "required": True}
    )
    message: str = field(
        metadata={
            "description": "Optional error message that provides more information",
            "required": False,
        }
    )


class UnknownPetId(HTTPError):
    status_code = 400
    message = "Unknown Pet identifier"
    extra_data = {"code": 1000}


class UnparsableRequestBody(HTTPError):
    status_code = 422
    message = "Could not read JSON body"
    extra_data = {"code": 2000}


class MissingRequestProperty(HTTPError):
    status_code = 400
    message = "Pet name is missing in request body"
    extra_data = {"code": 3000}


http_error_schema = {
    "type": "object",
    "required": ["code"],
    "properties": {"code": {"type": "string"}, "message": {"type": "string"}},
}

default_responses_schema = {
    "default": {
        "description": "Custom error",
        "content": {"application/json": {"schema": Error.Schema}},
    }
}
