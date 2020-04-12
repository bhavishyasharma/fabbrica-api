import mongoengine
from mongoengine.fields import ( StringField, DecimalField, ReferenceField, IntField, ListField )

class AclModel(mongoengine.Document):
    meta = {'collection': 'acl'}
    Id = StringField()
    username = StringField()
    clientid = StringField()
    publish = ListField(StringField())
    subscribe = ListField(StringField())
    pubsub = ListField(StringField())
