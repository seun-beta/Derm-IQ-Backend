from mongoengine import Document, connect

from app.config import settings

# Connect to MongoDB using MongoEngine
connect(db=settings.database_name, host=settings.database_url)


class Base(Document):
    meta = {"abstract": True}

