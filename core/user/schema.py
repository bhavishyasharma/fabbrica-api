import graphene
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from flask_jwt_extended import current_user, jwt_required
from role_decorators import admin_required
from .type import UserType
from .model import UserModel
from .mutations import RegisterUserMutation, AddUserRoleMutation, LoginMutation
from ..role.model import RoleModel
from core.common.type import Filter, Pagination

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    users = graphene.List(UserType, filters=graphene.List(Filter, required=False), 
        pagination=Pagination(required=False), sortings = graphene.List(graphene.String, required=False))
    users_count = graphene.Int(filters=graphene.List(Filter, required=False))

    @jwt_required
    @admin_required
    def resolve_users(self, info, filters=None, pagination:Pagination=None, sortings=None):
        if filters is None:
            qs = UserModel.objects()
        else:
            filter = {}
            for f in filters:
                filter[f.field+"__"+f.condition] = f.value
            qs = UserModel.objects(**filter)
        if pagination is not None:
            first = pagination.page * pagination.size
            qs = qs[first: first+pagination.size]
        if sortings is not None:
            qs = qs.order_by(*sortings)
        return list(qs.all())

    @jwt_required
    @admin_required
    def resolve_users_count(self, info, filters=None):
        if filters is None:
            qs = UserModel.objects()
        else:
            filter = {}
            for f in filters:
                filter[f.field+"__"+f.condition] = f.value
            qs = UserModel.objects(**filter)
        return qs.count()


class Mutation(graphene.ObjectType):
    register_user = RegisterUserMutation.Field()
    add_user_role = AddUserRoleMutation.Field()
    login = LoginMutation.Field()
 
schema = graphene.Schema(query=Query, types=[UserType], mutation=Mutation)