import graphene
from flask_jwt_extended import ( jwt_required )
from .type import MouldType
from .model import MouldModel

class AddMouldMutation(graphene.Mutation):
    mould = graphene.Field(MouldType)

    class Arguments:
        name = graphene.String(required=True)
        part = graphene.String(required=True)
        cavity = graphene.Int(required=True)
        runnerWeight = graphene.Decimal(required=True)

    @jwt_required
    def mutate(self, info, name, part, cavity, runnerWeight):
        mould = MouldModel(
            name = name,
            part = part,
            cavity = cavity,
            runnerWeight = runnerWeight
        )
        mould.save()
        return AddMouldMutation(mould=mould)