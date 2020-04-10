import graphene
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from .model import UserModel
from ..role.type import RoleInput, RoleType
from ..role.model import RoleModel

class UserType(MongoengineObjectType, graphene.ObjectType):
    class Meta:
        model = UserModel
        interfaces = (graphene.Node,)
    fullname = graphene.String()
    def resolve_fullname(parent, info):
        return f"{parent.firstname} {parent.lastname}"


class UserInput(graphene.InputObjectType):
    firstname = graphene.String()
    lastname = graphene.String()
    username = graphene.String()
    email = graphene.String()
    password = graphene.String()