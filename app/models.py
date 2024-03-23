from crud import Model
from pyrepositories import Entity

class Event(Model):
    date: str
    status: str
    max_attendees: int


class EventEntity(Entity):
    @property
    def date(self):
        return self.fields.get("date")
    @date.setter
    def date(self, value):
        self.fields["date"] = value
    @property
    def status(self):
        return self.fields.get("status")
    @status.setter
    def status(self, value):
        self.fields["status"] = value
    @property
    def max_attendees(self):
        return self.fields.get("max_attendees")
    @max_attendees.setter
    def max_attendees(self, value):
        self.fields["max_attendees"] = value
