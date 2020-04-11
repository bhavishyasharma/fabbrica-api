import mongoengine
from mongoengine.fields import ( StringField, DecimalField )

class PartModel(mongoengine.Document):
    meta = {'collection': 'part'}
    Id = StringField()
    name = StringField()
    material = StringField()
    color = StringField(required=False)
    weight = DecimalField()
