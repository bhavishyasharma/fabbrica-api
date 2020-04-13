import graphene
from flask_jwt_extended import ( jwt_required )
from .type import CompanyType
from .model import CompanyModel
from core.user.model import UserModel

class AddCompanyMutation(graphene.Mutation):
    company = graphene.Field(CompanyType)

    class Arguments:
        name = graphene.String(required=True)
        users = graphene.List(graphene.String)

    @jwt_required
    def mutate(self, info, name, users):
        company = CompanyModel(
            name = name,
            users = users
        )
        company.save()
        return AddCompanyMutation(company=company)

class UpdateCompanyMutation(graphene.Mutation):
    company = graphene.Field(CompanyType)

    class Arguments:
        companyId = graphene.String(required=True)
        name = graphene.String()
        users = graphene.List(graphene.String)

    @jwt_required
    def mutate(self, info, companyId, name=None, users=None):
        company = CompanyModel.objects(id=companyId).get()
        if name is not None:
            company.name = name
        if users is not None:
            usersList = UserModel.objects(id__in=users).all()
            company.users = usersList
        company.save()
        return UpdateCompanyMutation(company=company)