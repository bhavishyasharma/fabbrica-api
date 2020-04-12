import graphene
from flask_jwt_extended import (jwt_required)
from core.common.type import Filter, Pagination
from core.common.helpers import filter_qs, pagination_qs, sortings_qs
from .type import CompanyType
from .model import CompanyModel
from .mutations import AddCompanyMutation

class Query(graphene.ObjectType):
    companies = graphene.List(CompanyType, filters=graphene.List(Filter, required=False), 
        pagination=Pagination(required=False), sortings = graphene.List(graphene.String, required=False))
    
    @jwt_required
    def resolve_companies(self, info, filters=None, pagination=None, sortings=None):
        qs = CompanyModel.objects()
        qs = filter_qs(qs, filters)
        qs = pagination_qs(qs, pagination)
        qs = sortings_qs(qs, sortings)
        return list(CompanyModel.objects().all())

class Mutation(graphene.ObjectType):
    add_company = AddCompanyMutation.Field()

schema = graphene.Schema(query=Query, types=[CompanyType], mutation=Mutation)