from .models import Brand, Model
from .schemas import BrandSchema, ModelSchema
from .publisher import Publisher


def _publish(model, message, action):
    Publisher.publish(model.__name__.lower(), message, action)


def get_objects(model):
    return model.objects.all()


def get_object(model, **kwargs):
    return model.objects.get(**kwargs)


def create_object(model, **kwargs):
    obj = model.objects.create(**kwargs)
    _publish(model, kwargs, "added")
    return obj


def delete_object(model, pk):
    obj = model.objects.get(pk=pk)
    json = BrandSchema.from_orm(obj).dict()
    _publish(model, json, "deleted")
