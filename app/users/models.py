from sqlalchemy import Column, Integer, String

from app.commons.base_model import TimeStampedBaseModel


class User(TimeStampedBaseModel):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(256), nullable=False)
    last_name = Column(String(256), nullable=False)
    email_address = Column(String(256), nullable=False, unique=True)
    mobile_number = Column(String(30), nullable=False, unique=True)
    password = Column(String(256), nullable=False)
