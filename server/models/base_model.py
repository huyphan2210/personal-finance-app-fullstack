from datetime import datetime
from enum import EnumMeta
from typing import get_origin, get_args, List, Type
from pydantic import BaseModel as PydanticBaseModel
from flask_restx import fields, Namespace

TYPE_MAP = {
    str: fields.String,
    int: fields.Integer,
    float: fields.Float,
    bool: fields.Boolean,
    datetime: fields.String,
}


class BaseModel(PydanticBaseModel):
    @classmethod
    def get_api_model(cls, ns: Namespace):
        model_fields = {}
        for name, model_field in cls.model_fields.items():
            field_type: Type = model_field.annotation
            origin = get_origin(field_type)
            args = get_args(field_type)

            # Handle List[BaseModel]
            if origin in (list, List):
                item_type = args[0]
                if isinstance(item_type, type) and issubclass(item_type, BaseModel):
                    nested_model = item_type.get_api_model(ns)
                    model_fields[name] = fields.List(
                        fields.Nested(nested_model),
                        required=model_field.is_required(),
                        description=model_field.description or "",
                    )
                    continue
                elif item_type in TYPE_MAP:
                    model_fields[name] = fields.List(
                        TYPE_MAP[item_type](),
                        required=model_field.is_required(),
                        description=model_field.description or "",
                    )
                    continue
                else:
                    raise TypeError(f"Unsupported list item type: {item_type}")

            # Case 1: field is a nested Pydantic model
            if isinstance(field_type, type) and issubclass(field_type, BaseModel):
                nested_model = field_type.get_api_model(ns)
                model_fields[name] = fields.Nested(
                    nested_model, required=model_field.is_required()
                )
                continue

            # Case 2: field is an enum
            if isinstance(field_type, type) and isinstance(field_type, EnumMeta):
                enum_values = [e.value for e in field_type]

                field_class = (
                    fields.String if isinstance(enum_values[0], str) else fields.Integer
                )

                model_fields[name] = field_class(
                    required=model_field.is_required(),
                    description=model_field.description or f"One of: {enum_values}",
                    enum=enum_values,
                )
                continue

            # Case 3: field is a primitive
            restx_field = TYPE_MAP.get(field_type)
            if not restx_field:
                raise TypeError(
                    f"Unsupported field type: {field_type} for field '{name}'"
                )

            model_fields[name] = restx_field(
                required=model_field.is_required(),
                description=model_field.description,
            )

        return ns.model(cls.__name__, model_fields)
