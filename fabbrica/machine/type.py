import graphene
from graphene_mongo import MongoengineObjectType
from .model import MachineModel

class MachineType(MongoengineObjectType, graphene.ObjectType):
    class Meta:
        model = MachineModel
        