#! /usr/bin/env python

import logging
import re

from apiflask import APIFlask
from apiflask.schemas import EmptySchema

from flask import request, jsonify, make_response

from pet import Pet
from pet_properties import PetProperties
from error import (
    default_responses_schema,
    http_error_schema,
    UnknownPetId,
    MissingRequestProperty,
)


class ContentHeaderCheck:
    """Flask middleware that checks for Accept and Content-type headers"""

    def before_request(self):
        # API only supports JSON-encoded requests and responses
        supported_media_type = "application/json"

        if request.method == "POST":
            # Check for supported media type and return the "Unsupported Media Type" return code if incorrect
            if request.headers.get("Content-Type") != supported_media_type:
                return jsonify(
                    {
                        "code": 4000,
                        "message": "Content-Type must be {}".format(
                            supported_media_type
                        ),
                    }
                ), 415

        if request.method == "GET":
            accept_header_value = request.headers.get("Accept")

            # Check for supported media type and return the "Not Acceptable" return code if incorrect
            if (
                accept_header_value is not None
                and accept_header_value != supported_media_type
                and not re.match(r"\*/\*", accept_header_value)
            ):
                return jsonify(
                    {
                        "code": 4000,
                        "message": "Accept header must be {}".format(
                            supported_media_type
                        ),
                    }
                ), 406


# Application config including OpenAPI version, title, description and API version
app = APIFlask(
    __name__,
    title="OpenAPI v3.1 Fundamentals Example",
    version="1.0.0",
)
app.config["DESCRIPTION"] = (
    "A stripped-down version of the Petstore API for the OpenAPI v3.1 Fundamentals course."
)
app.config["OPENAPI_VERSION"] = "3.1.0"

# Disable default behaviours that are not required
app.config["AUTO_404_RESPONSE"] = False
app.config["AUTO_VALIDATION_ERROR_RESPONSE"] = False


# Root tags object
app.config["TAGS"] = [
    {"name": "GET", "description": "HTTP GET operations"},
    {"name": "POST", "description": "HTTP POST operations"},
    {
        "name": "Read Pet(s)",
        "description": "Retrieve the properties of one-or-more pets based on the requested URI",
    },
    {
        "name": "Create a Pet",
        "description": "Create a new Pet resource in the Petstore collection",
    },
]

app.config["HTTP_ERROR_SCHEMA"] = http_error_schema
app.config["VALIDATION_ERROR_SCHEMA"] = http_error_schema

# Register middleware
middleware = ContentHeaderCheck()
app.before_request(middleware.before_request)

# Globals used for simple example
PETS = {
    "1": Pet(
        "Barnaby",
        "Vicious",
        "1",
    ),
    "2": Pet("Colin", "Accountant", "2"),
}
LAST_PET_ID = 2


@app.error_processor
def error_processor(error):
    """Custom error processor that suppresses the built-in detail property"""

    code = error.extra_data.get("code")

    return (
        {
            "code": code if code is not None else -1,
            "message": error.message,
        },
        error.status_code,
        error.headers,
    )


@app.post("/pets")
@app.doc(
    operation_id="CreatePet",
    tags=["POST", "Create a Pet"],
    responses=default_responses_schema,
)
@app.input(PetProperties.Schema)
@app.output(EmptySchema, status_code=201)
def post_pets(json):
    """Create a new Pet

    Add a new Pet to the collection of pets at the Petstore API
    """

    global LAST_PET_ID
    global PETS

    # Belt-and-braces check but probably not necessary
    if json.name is None:
        raise MissingRequestProperty

    LAST_PET_ID = LAST_PET_ID + 1
    new_pet = Pet(LAST_PET_ID, json.name, json.tag)
    PETS[LAST_PET_ID] = new_pet

    return make_response("", 201)


@app.route("/pets", methods=["GET"])
@app.doc(
    operation_id="RetrievePets",
    tags=["GET", "Read Pet(s)"],
    responses=default_responses_schema,
)
@app.output(Pet.Schema(many=True))
def get_pets():
    """Get all Pets

    Retrieve all Pets available at Petstore API
    """

    return [
        {
            key: pet.__dict__[key]
            for key in pet.__dict__
            if pet.__dict__[key] is not None
        }
        for pet in PETS.values()
    ]


@app.route("/pets/<petId>", methods=["GET"])
@app.doc(
    operation_id="RetrievePet",
    tags=["GET", "Read Pet(s)"],
    responses=default_responses_schema,
)
@app.output(Pet.Schema, status_code=200)
def get_pet(petId):
    """Get a Pet

    Retrieve a Pet based on the petId from the Petstore API
    """

    requested_pet = PETS.get(petId)

    if requested_pet is None:
        raise UnknownPetId

    return jsonify(requested_pet.__dict__)


if __name__ == "__main__":
    app.logger.setLevel(logging.DEBUG)
    app.logger.info("Starting Flask server...")

    # Start the Flask application
    app.run(debug=True, port=5001)
