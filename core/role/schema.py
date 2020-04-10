import graphene
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from .type import RoleType
from .model import RoleModel
from .mutations import AddRoleMutation

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    roles = MongoengineConnectionField(RoleType)
    role = graphene.Field(RoleType)
    def resolve_roles(self, info):
        return list(RoleModel.objects.all())

    def resolve_role(self, info, id=None):
        return RoleModel.objects.filter(id=id)

class Mutation(graphene.ObjectType):
    add_role = AddRoleMutation.Field()
 
schema = graphene.Schema(query=Query, types=[RoleType], mutation=Mutation)