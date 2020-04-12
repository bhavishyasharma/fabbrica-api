import graphene
from flask_jwt_extended import ( jwt_required )
from .type import CompanyType
from .model import CompanyModel

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