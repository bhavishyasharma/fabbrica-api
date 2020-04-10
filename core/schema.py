import graphene
from .user.schema import schema as UserSchema
from .role.schema import schema as RoleSchema

class Query(UserSchema.Query, RoleSchema.Query, graphene.ObjectType):
    pass

class Mutation(UserSchema.Mutation, RoleSchema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)