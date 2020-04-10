import graphene
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from .model import RoleModel

class RoleType(MongoengineObjectType, graphene.ObjectType):
    class Meta:
        model = RoleModel

class AddRoleInput(graphene.InputObjectType):
    name = graphene.String()

    