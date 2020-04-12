import graphene
from graphene_mongo import MongoengineObjectType
from .model import CompanyModel

class CompanyType(MongoengineObjectType, graphene.ObjectType):
    class Meta:
        model = CompanyModel
        