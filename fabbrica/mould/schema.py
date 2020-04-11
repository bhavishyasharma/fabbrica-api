import graphene
from flask_jwt_extended import (jwt_required)
from core.common.type import Filter, Pagination
from core.common.helpers import filter_qs, pagination_qs, sortings_qs
from .type import MouldType
from .model import MouldModel
from .mutations import AddMouldMutation

class Query(graphene.ObjectType):
    moulds = graphene.List(MouldType, filters=graphene.List(Filter, required=False), 
        pagination=Pagination(required=False), sortings = graphene.List(graphene.String, required=False))
    
    @jwt_required
    def resolve_moulds(self, info, filters=None, pagination=None, sortings=None):
        qs = MouldModel.objects()
        qs = filter_qs(qs, filters)
        qs = pagination_qs(qs, pagination)
        qs = sortings_qs(qs, sortings)
        return list(MouldModel.objects().all())

class Mutation(graphene.ObjectType):
    add_mould = AddMouldMutation.Field()

schema = graphene.Schema(query=Query, types=[MouldType], mutation=Mutation)