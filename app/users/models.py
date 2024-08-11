from mongoengine import EmailField, StringField

from app.commons.base_model import TimeStampedBaseModel


class User(TimeStampedBaseModel):
    first_name = StringField(max_length=256, required=True)
    last_name = StringField(max_length=256, required=True)
    email_address = EmailField(required=True, unique=True)
    mobile_number = StringField(max_length=30, required=True, unique=True)
    password = StringField(max_length=256, required=True)
