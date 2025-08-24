from http import HTTPStatus
from flask import jsonify, request
from flask_restx import Namespace, Resource, fields

from enums.color_enum import Color
from exceptions import BadRequestError, NotFoundError
from services.pots_service import delete_pot, get_pots, create_pot, update_pot
from models.pots_model import CreatePotDto, DeletePotDto, Pots, UpdatePotDto

POTS = "pots-api"
pots_ns = Namespace(f"{POTS}", description="Get Pots content")


create_pot_dto = pots_ns.model(
    "CreatePot",
    {
        "name": fields.String(
            required=True, description="Name of the pot", min_length=1, max_length=30
        ),
        "colorTheme": fields.String(
            required=True,
            description="Pot color theme",
            enum=[e.value for e in Color],
        ),
        "target": fields.Float(required=True, description="Maximum target of the pot"),
        "total": fields.Float(required=False, description="Total of the pot"),
    },
)

delete_pot_dto = pots_ns.model(
    "DeletePot", {"id": fields.String(required=True, description="Pot ID (UUID)")}
)

update_pot_dto = pots_ns.model(
    "UpdatePot",
    {
        **delete_pot_dto,
        "name": fields.String(
            required=False, description="Name of the pot", min_length=1, max_length=30
        ),
        "colorTheme": fields.String(
            required=False,
            description="Pot color theme",
            enum=[e.value for e in Color],
        ),
        "target": fields.Float(required=False, description="Maximum target of the pot"),
        "total": fields.Float(required=False, description="Total of the pot"),
    },
)


class PotsApi(Resource):
    @pots_ns.doc(description="Get the pots data")
    @pots_ns.response(HTTPStatus.OK, "Success", model=Pots.get_api_model(pots_ns))
    def get(self):
        pots = get_pots()
        return jsonify(pots.model_dump())

    @pots_ns.doc(description="Create new pot")
    @pots_ns.expect(create_pot_dto)
    @pots_ns.response(HTTPStatus.CREATED, "Created")
    @pots_ns.response(HTTPStatus.BAD_REQUEST, "Invalid input")
    def post(self):
        requestBody = request.get_json()
        try:
            try:
                create_pot_dto = CreatePotDto(**requestBody)
            except ValueError as e:
                raise BadRequestError(str(e))
            create_pot(create_pot_dto)
        except BadRequestError as e:
            return e.args[0], HTTPStatus.BAD_REQUEST

        return "Created", HTTPStatus.CREATED

    @pots_ns.doc(description="Update pot")
    @pots_ns.expect(update_pot_dto)
    @pots_ns.response(HTTPStatus.OK, "Updated")
    @pots_ns.response(HTTPStatus.BAD_REQUEST, "Invalid input")
    def patch(self):
        requestBody = request.get_json()
        try:
            try:
                update_pot_dto = UpdatePotDto(**requestBody)
            except ValueError as e:
                raise BadRequestError(str(e))
            update_pot(update_pot_dto)
        except BadRequestError as e:
            return e.args[0], HTTPStatus.BAD_REQUEST
        except NotFoundError as e:
            return e.args[0], HTTPStatus.NOT_FOUND

        return "Updated", HTTPStatus.OK

    @pots_ns.doc(description="Delete pot")
    @pots_ns.expect(delete_pot_dto)
    @pots_ns.response(HTTPStatus.OK, "Deleted")
    @pots_ns.response(HTTPStatus.BAD_REQUEST, "Invalid input")
    def delete(self):
        requestBody = request.get_json()
        try:
            try:
                delete_pot_dto = DeletePotDto(**requestBody)
            except ValueError as e:
                raise BadRequestError(str(e))
            delete_pot(delete_pot_dto)
        except BadRequestError as e:
            return e.args[0], HTTPStatus.BAD_REQUEST
        except NotFoundError as e:
            return e.args[0], HTTPStatus.NOT_FOUND

        return "Deleted", HTTPStatus.OK


pots_ns.add_resource(PotsApi, "")
