from typing import Type
from pydantic import BaseModel as PydanticBaseModel
from flask_restx import fields, Api

TYPE_MAP = {
    str: fields.String,
    int: fields.Integer,
    float: fields.Float,
    bool: fields.Boolean,
}


class BaseModel(PydanticBaseModel):
    @classmethod
    def get_api_model(cls, api: Api):
        model_fields = {}
        for name, model_field in cls.model_fields.items():
            field_type: Type = model_field.annotation

            # Case 1: field is a nested Pydantic model
            if isinstance(field_type, type) and issubclass(field_type, BaseModel):
                nested_model = field_type.get_api_model(api)
                model_fields[name] = fields.Nested(
                    nested_model, required=model_field.is_required()
                )
                continue

            # Case 2: field is a primitive
            restx_field = TYPE_MAP.get(field_type)
            if not restx_field:
                raise TypeError(
                    f"Unsupported field type: {field_type} for field '{name}'"
                )

            model_fields[name] = restx_field(
                required=model_field.is_required(),
                description=model_field.description,
            )

        return api.model(cls.__name__, model_fields)
