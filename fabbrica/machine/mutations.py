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

class UpdateMachineMutation(graphene.Mutation):
    machine = graphene.Field(MachineType)

    class Arguments:
        machineId = graphene.String(required=True)
        name = graphene.String()
        make = graphene.String()
        model = graphene.String()
        company = graphene.String()
        clampingCapacity = graphene.Int()
        injectionVolume = graphene.Decimal()

    @jwt_required
    def mutate(self, info, machineId, name=None, make=None, model=None, company=None, clampingCapacity=None, injectionVolume=None):
        machine = MachineModel.objects(id=machineId).get()
        companyDocument = None
        if name is not None:
            machine.name = name
        if make is not None:
            machine.make = make
        if model is not None:
            machine.model = model
        if company is not None:
            companyDocument = CompanyModel.objects(id=company).get()
            machine.company = companyDocument
        if clampingCapacity is not None:
            machine.clampingCapacity = clampingCapacity
        if injectionVolume is not None:
            machine.injectionVolume = injectionVolume
        machine.save()
        if companyDocument is not None:
            updateAcl(companyDocument)
        return UpdateMachineMutation(machine=machine)