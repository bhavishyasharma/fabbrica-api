import graphene
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from .type import UserType
from .model import UserModel
from .mutations import RegisterUserMutation, AddUserRoleMutation
from ..role.model import RoleModel

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    users = MongoengineConnectionField(UserType)
    def resolve_users(self, info):
        return list(UserModel.objects.all())

class Mutation(graphene.ObjectType):
    register_user = RegisterUserMutation.Field()
    add_user_role = AddUserRoleMutation.Field()
 
schema = graphene.Schema(query=Query, types=[UserType], mutation=Mutation)