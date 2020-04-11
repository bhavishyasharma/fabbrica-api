import mongoengine
from mongoengine.fields import ( StringField, DecimalField, ReferenceField, IntField )

class MachineModel(mongoengine.Document):
    meta = {'collection': 'machine'}
    Id = StringField()
    name = StringField()
    make = StringField()
    model = StringField()
    clampingCapacity = IntField()
    injectionVolume = DecimalField()
