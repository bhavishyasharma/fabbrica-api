import graphene
from flask_jwt_extended import ( jwt_required )
from fabbrica.company.model import CompanyModel
from .type import MachineType
from .model import MachineModel
from fabbrica.company.helpers import updateAcl

class AddMachineMutation(graphene.Mutation):
    machine = graphene.Field(MachineType)

    class Arguments:
        name = graphene.String(required=True)
        make = graphene.String(required=True)
        model = graphene.String(required=True)
        company = graphene.String(required=True)
        clampingCapacity = graphene.Int(required=True)
        injectionVolume = graphene.Decimal(required=True)

    @jwt_required
    def mutate(self, info, name, make, model, company, clampingCapacity, injectionVolume):
        machine = MachineModel(
            name = name,
            make = make,
            model = model,
            company = company,
            clampingCapacity = clampingCapacity,
            injectionVolume = injectionVolume
        )
        machine.save()
        company = CompanyModel.objects(id=company).get()
        updateAcl(company)
        return AddMachineMutation(machine=machine)