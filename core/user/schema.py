import graphene
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from flask_jwt_extended import current_user, jwt_required
from role_decorators import admin_required
from .type import UserType
from .model import UserModel
from .mutations import RegisterUserMutation, AddUserRoleMutation, LoginMutation
from ..role.model import RoleModel

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    users = graphene.List(UserType)

    @jwt_required
    @admin_required
    def resolve_users(self, info):
        return list(UserModel.objects.all())

class Mutation(graphene.ObjectType):
    register_user = RegisterUserMutation.Field()
    add_user_role = AddUserRoleMutation.Field()
    login = LoginMutation.Field()
 
schema = graphene.Schema(query=Query, types=[UserType], mutation=Mutation)