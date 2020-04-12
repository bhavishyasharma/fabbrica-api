import mongoengine
from mongoengine.fields import ( StringField, DecimalField, ReferenceField, IntField, ListField )
from core.user.model import UserModel

class CompanyModel(mongoengine.Document):
    meta = {'collection': 'company'}
    Id = StringField()
    name = StringField()
    users = ListField(ReferenceField(UserModel, reverse_delete_rule=mongoengine.DENY))
