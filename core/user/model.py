import mongoengine
from mongoengine import Document
from mongoengine.fields import (
    ObjectIdField, EmailField, DateTimeField, ReferenceField, StringField, ListField
)
import bcrypt
from ..role.model import RoleModel

class UserModel(Document):
    meta = {'collection': 'user'}
    _id = ObjectIdField()
    firstname = StringField()
    lastname = StringField()
    email = EmailField(unique=True)
    username = StringField(unique=True)
    password = StringField()
    roles = ReferenceField(RoleModel, reverse_delete_rule=mongoengine.DENY)

    def setPassword(self,password):
        self.password = (bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())).decode("utf-8") 

    def addRole(self, role):
        self.roles.append(role)
