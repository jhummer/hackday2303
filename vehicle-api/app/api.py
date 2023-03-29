from typing import List
from ninja import NinjaAPI

from .models import Brand, Model
from .schemas import BrandSchema, ModelSchema
from .services import create_object, get_objects, delete_object


api = NinjaAPI()


@api.get("/healthcheck")
def healthcheck(request):
    return "feeling good..."


@api.get("/brands", response=List[BrandSchema])
def brands(request):
    return get_objects(Brand)


@api.post("/brands", response=BrandSchema)
def create_brand(request, payload: BrandSchema):
    brand = create_object(Brand, **payload.dict())
    return brand


@api.delete("/brands/{brand_id}")
def create_brand(request, brand_id: int):
    delete_object(Brand, brand_id)


@api.get("/models", response=List[ModelSchema])
def brands(request):
    return get_objects(Model)
