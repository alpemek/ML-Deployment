from mongoengine import *
import datetime
import os

DB_NAME = os.environ.get("DB_NAME")
DB_HOST = os.environ.get("DB_HOST")

connect(DB_NAME, host=DB_HOST)

class Job(Document):

    time_created = DateTimeField(default=datetime.datetime.utcnow)
    state = StringField(default="Initialized", choices=["Initialized", "Processing", "Completed", "Failed"])
    source = StringField(required=True)
    result = ListField()

    def to_dict(self):
        return {
            "id": str(self.id),
            "state": str(self.state),
            "time_created": str(self.time_created),
            "result": list(self.result)
        }