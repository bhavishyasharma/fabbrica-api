from mongoengine import Document
from mongoengine.fields import StringField, ObjectIdField

class RoleModel(Document):
    meta = {'collection': 'role'}
    _id = ObjectIdField()
    name = StringField(unique=True)
    label = StringField()