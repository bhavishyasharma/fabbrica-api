import graphene
from graphene_mongo import MongoengineObjectType
from .model import MouldModel

class MouldType(MongoengineObjectType, graphene.ObjectType):
    class Meta:
        model = MouldModel
        