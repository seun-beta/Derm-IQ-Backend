from datetime import datetime

from mongoengine import (DateTimeField, FloatField, ListField, ReferenceField,
                         StringField)

from app.commons.base_model import TimeStampedBaseModel
from app.users.models import User
from products.models import Product


class CartItem(TimeStampedBaseModel):
    user = ReferenceField(User, required=True)
    product = ReferenceField(Product, required=True)
    quantity = FloatField(required=True)


class Order(TimeStampedBaseModel):
    user = ReferenceField(User, required=True)
    items = ListField(ReferenceField(CartItem), required=True)
    total_price = FloatField(required=True)
    created_at = DateTimeField(default=datetime.now)
    status = StringField(default="pending")
