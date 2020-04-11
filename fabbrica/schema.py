import graphene
from .part.schema import schema as PartSchema
from .mould.schema import schema as MouldSchema

class Query(PartSchema.Query, MouldSchema.Query, graphene.ObjectType):
    pass

class Mutation(PartSchema.Mutation, MouldSchema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)