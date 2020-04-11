import graphene
from graphene_mongo import MongoengineObjectType
from .model import PartModel

class PartType(MongoengineObjectType, graphene.ObjectType):
    class Meta:
        model = PartModel
        