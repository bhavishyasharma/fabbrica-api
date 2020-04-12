import graphene
from .part.schema import schema as PartSchema
from .mould.schema import schema as MouldSchema
from .machine.schema import schema as MachineSchema
from .company.schema import schema as CompanySchema

class Query(PartSchema.Query, MouldSchema.Query, MachineSchema.Query, CompanySchema.Query, graphene.ObjectType):
    pass

class Mutation(PartSchema.Mutation, MouldSchema.Mutation, MachineSchema.Mutation, CompanySchema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)