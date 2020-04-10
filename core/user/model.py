import mongoengine
from mongoengine import Document
from mongoengine.fields import (
    ObjectIdField, EmailField, DateTimeField, ReferenceField, StringField, ListField
)
import bcrypt
from ..role.model import RoleModel

class UserModel(Document):
    meta = {'collection': 'user'}
    Id = StringField()
    firstname = StringField()
    lastname = StringField()
    email = EmailField(unique=True)
    username = StringField(unique=True)
    password = StringField()
    roles = ListField(ReferenceField(RoleModel, reverse_delete_rule=mongoengine.DENY))

    def setPassword(self,password):
        self.password = (bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())).decode("utf-8") 

    def verifyPassword(self, password):
        if(bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))):
            return True
        return False

    def addRole(self, role):
        self.roles.append(role)
