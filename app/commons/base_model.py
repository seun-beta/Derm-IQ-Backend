from datetime import datetime

from mongoengine import DateTimeField, Document


class TimeStampedBaseModel(Document):
    meta = {"abstract": True}
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        return super(TimeStampedBaseModel, self).save(*args, **kwargs)
