import graphene
from graphql import GraphQLError
from mongoengine.errors import DoesNotExist
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity
)
from role_decorators import admin_required
from .type import UserType, LoginInput, TokenOutput, RefreshOutput
from .model import UserModel
from .mutations import RegisterUserMutation, AddUserRoleMutation
from ..role.model import RoleModel
from core.common.type import Filter, Pagination

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    users = graphene.List(UserType, filters=graphene.List(Filter, required=False), 
        pagination=Pagination(required=False), sortings = graphene.List(graphene.String, required=False))
    users_count = graphene.Int(filters=graphene.List(Filter, required=False))
    login = graphene.Field(TokenOutput, login_data = LoginInput(required=True))
    refresh = graphene.Field(RefreshOutput)

    def resolve_login(self, info, login_data=None):
        try:
            user = UserModel.objects(username=login_data.username).get()
            if(user.verifyPassword(login_data.password)):
                token = TokenOutput(
                    user = user,
                    access_token = create_access_token(identity=user),
                    refresh_token = create_refresh_token(identity=user)
                )
                return token
            else:
                raise GraphQLError('Invalid username or password')
        except DoesNotExist:
            raise GraphQLError('Invalid username or password')

    @jwt_refresh_token_required
    def resolve_refresh(self, info):
        current_user = get_jwt_identity()
        user = UserModel.objects(username=current_user['username']).get()
        return RefreshOutput(access_token= create_access_token(identity=user))

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
 
schema = graphene.Schema(query=Query, types=[UserType], mutation=Mutation)