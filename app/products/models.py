from mongoengine import FloatField, ListField, StringField

from app.commons.base_model import TimeStampedBaseModel


class Product(TimeStampedBaseModel):
    name = StringField(max_length=256, required=True)
    description = StringField(max_length=1024, required=True)
    price = FloatField(required=True)
    ingredients = ListField(StringField(), required=True)
    skin_type = ListField(
        StringField(), required=True
    )  # e.g., ['oily', 'dry', 'sensitive']
