import graphene
from flask_jwt_extended import (jwt_required)
from core.common.type import Filter, Pagination
from core.common.helpers import filter_qs, pagination_qs, sortings_qs
from .type import MachineType
from .model import MachineModel
from .mutations import AddMachineMutation

class Query(graphene.ObjectType):
    machines = graphene.List(MachineType, filters=graphene.List(Filter, required=False), 
        pagination=Pagination(required=False), sortings = graphene.List(graphene.String, required=False))
    
    @jwt_required
    def resolve_machines(self, info, filters=None, pagination=None, sortings=None):
        qs = MachineModel.objects()
        qs = filter_qs(qs, filters)
        qs = pagination_qs(qs, pagination)
        qs = sortings_qs(qs, sortings)
        return list(MachineModel.objects().all())

class Mutation(graphene.ObjectType):
    add_machine = AddMachineMutation.Field()

schema = graphene.Schema(query=Query, types=[MachineType], mutation=Mutation)