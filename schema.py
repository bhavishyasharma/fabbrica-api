import graphene
import core.schema
import fabbrica.schema

class Query(core.schema.Query, fabbrica.schema.Query, graphene.ObjectType):
    pass

class Mutation(core.schema.Mutation, fabbrica.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)