import graphene
from .part.schema import schema as PartSchema

class Query(PartSchema.Query, graphene.ObjectType):
    pass

class Mutation(PartSchema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)