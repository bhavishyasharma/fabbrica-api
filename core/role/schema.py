import graphene
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from flask_jwt_extended import current_user, jwt_required
from role_decorators import admin_required
from .type import RoleType
from .model import RoleModel
from .mutations import AddRoleMutation

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    roles = graphene.List(RoleType)
    role = graphene.Field(RoleType, id=graphene.String(required=True))

    @jwt_required
    @admin_required
    def resolve_roles(self, info):
        return list(RoleModel.objects.all())

    @jwt_required
    def resolve_role(self, info, id=None):
        return RoleModel.objects.filter(id=id)

class Mutation(graphene.ObjectType):
    add_role = AddRoleMutation.Field()
 
schema = graphene.Schema(query=Query, types=[RoleType], mutation=Mutation)