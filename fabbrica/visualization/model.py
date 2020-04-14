import mongoengine
from mongoengine.fields import ( StringField, IntField, ListField )

class VisualizationModel(mongoengine.Document):
    meta = {'collection': 'visualization'}
    Id = StringField()
    name = StringField()
    parentType = StringField()
    visualizationType = StringField()
    query = StringField()
    parameters = ListField(StringField())
    width = IntField()
