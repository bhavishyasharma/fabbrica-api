import graphene
from graphene_mongo import MongoengineObjectType
from .model import PartModel
from ..mould.type import MouldType
from ..mould.model import MouldModel

class PartType(MongoengineObjectType, graphene.ObjectType):
    class Meta:
        model = PartModel
    moulds = graphene.List(MouldType)

    def resolve_moulds(parent, info):
        return MouldModel.objects(part=str(parent.id)).all()
        