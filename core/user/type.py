import graphene
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from .model import UserModel

class UserType(MongoengineObjectType, graphene.ObjectType):
    class Meta:
        model = UserModel
    fullname = graphene.String()
    def resolve_fullname(parent, info):
        return f"{parent.firstname} {parent.lastname}"

    def resolve_id(parent, info):
        return parent.id

class UserInput(graphene.InputObjectType):
    firstname = graphene.String()
    lastname = graphene.String()
    username = graphene.String()
    email = graphene.String()
    password = graphene.String()

class LoginInput(graphene.InputObjectType):
    username = graphene.String()
    password = graphene.String()

class TokenOutput(graphene.ObjectType):
    user = graphene.Field(UserType)
    access_token = graphene.String()
    refresh_token = graphene.String()

class RefreshOutput(graphene.ObjectType):
    access_token = graphene.String()