import graphene
from flask_jwt_extended import ( jwt_required )
from .type import MouldType
from .model import MouldModel
from ..part.model import PartModel
from ..company.model import CompanyModel

class AddMouldMutation(graphene.Mutation):
    mould = graphene.Field(MouldType)

    class Arguments:
        name = graphene.String(required=True)
        company = graphene.String(required=True)
        part = graphene.String(required=True)
        cavity = graphene.Int(required=True)
        runnerWeight = graphene.Decimal(required=True)

    @jwt_required
    def mutate(self, info, name, company, part, cavity, runnerWeight):
        mould = MouldModel(
            name = name,
            company = company,
            part = part,
            cavity = cavity,
            runnerWeight = runnerWeight
        )
        mould.save()
        return AddMouldMutation(mould=mould)

class UpdateMouldMutation(graphene.Mutation):
    mould = graphene.Field(MouldType)

    class Arguments:
        mouldId = graphene.String(required=True)
        name = graphene.String()
        company = graphene.String()
        part = graphene.String()
        cavity = graphene.Int()
        runnerWeight = graphene.Decimal()

    @jwt_required
    def mutate(self, info, mouldId, name=None, company=None, part=None, cavity=None, runnerWeight=None):
        mould = MouldModel.objects(id=mouldId).get()
        if name is not None:
            mould.name = name
        if company is not None:
            companyDocument = CompanyModel.objects(id=company).get()
            mould.company = companyDocument
        if part is not None:
            partDocument = PartModel.objects(id=part).get()
            mould.part = partDocument
        if cavity is not None:
            mould.cavity = cavity
        if runnerWeight is not None:
            mould.runnerWeight = runnerWeight
        mould.save()
        return UpdateMouldMutation(mould=mould)
