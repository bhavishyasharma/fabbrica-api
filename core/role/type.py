import graphene
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from .model import RoleModel

class RoleType(MongoengineObjectType, graphene.ObjectType):
    class Meta:
        model = RoleModel
        interfaces = (graphene.Node,)

class RoleInput(graphene.InputObjectType):
    _id = graphene.String()
    name = graphene.String()

class AddRoleInput(graphene.InputObjectType):
    name = graphene.String()

    