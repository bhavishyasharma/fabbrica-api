import graphene
from flask_jwt_extended import ( jwt_required )
from .type import MachineType
from .model import MachineModel

class AddMachineMutation(graphene.Mutation):
    machine = graphene.Field(MachineType)

    class Arguments:
        name = graphene.String(required=True)
        make = graphene.String(required=True)
        model = graphene.String(required=True)
        clampingCapacity = graphene.Int(required=True)
        injectionVolume = graphene.Decimal(required=True)

    @jwt_required
    def mutate(self, info, name, make, model, clampingCapacity, injectionVolume):
        machine = MachineModel(
            name = name,
            make = make,
            model = model,
            clampingCapacity = clampingCapacity,
            injectionVolume = injectionVolume
        )
        machine.save()
        return AddMachineMutation(machine=machine)