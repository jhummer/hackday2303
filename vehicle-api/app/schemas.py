from ninja import ModelSchema

from .models import Brand, Model


class BrandSchema(ModelSchema):
    class Config:
        model = Brand
        model_fields = "__all__"


class ModelSchema(ModelSchema):
    class Config:
        model = Model
        model_fields = "__all__"
