import graphene
from flask_jwt_extended import (jwt_required)
from core.common.type import Filter, Pagination
from .type import PartType
from .model import PartModel
from .mutations import AddPartMutation

class Query(graphene.ObjectType):
    parts = graphene.List(PartType, filters=graphene.List(Filter, required=False), 
        pagination=Pagination(required=False), sortings = graphene.List(graphene.String, required=False))
    
    @jwt_required
    def resolve_parts(self, info, filters=None, pagination=None, sortings=None):
        return list(PartModel.objects().all())

class Mutation(graphene.ObjectType):
    add_part = AddPartMutation.Field()

schema = graphene.Schema(query=Query, types=[PartType], mutation=Mutation)