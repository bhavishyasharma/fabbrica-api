import mongoengine
from mongoengine.fields import ( StringField, DecimalField, ReferenceField, IntField )
from ..part.model import PartModel

class MouldModel(mongoengine.Document):
    meta = {'collection': 'mould'}
    Id = StringField()
    name = StringField()
    part = ReferenceField(PartModel, reverse_delete_rule=mongoengine.DENY)
    cavity = IntField()
    runnerWeight = DecimalField()
