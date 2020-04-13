import graphene
from graphql import GraphQLError
from mongoengine.errors import DoesNotExist
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity
)
from .type import UserType, UserInput, LoginInput, TokenOutput
from .model import UserModel
from ..role.model import RoleModel
from role_decorators import admin_required

class RegisterUserMutation(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        user_data = UserInput(required=True)

    def mutate(self, info, user_data=None):
        userRole = RoleModel.objects(name="user").get()
        user = UserModel(
            firstname = user_data.firstname,
            lastname = user_data.lastname,
            username = user_data.username,
            email = user_data.email,
            roles = [userRole]
        )
        user.setPassword(user_data.password)
        user.save()
        return RegisterUserMutation(user=user)

class UpdateUserMutation(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        userId = graphene.String(required=True)
        username = graphene.String()
        email = graphene.String()
        firstname = graphene.String()
        lastname = graphene.String()
        roles = graphene.List(graphene.String)

    def mutate(self, info, userId, username=None, email=None, firstname=None, lastname=None, roles=None):
        user = UserModel.objects(id=userId).get()
        if username is not None:
            user.username = username
        if email is not None:
            user.email = email
        if firstname is not None:
            user.firstname = firstname
        if lastname is not None:
            user.lastname = lastname
        if roles is not None:
            rolesList = RoleModel.objects(id__in=roles).all()
            user.roles = rolesList
        user.save()
        return UpdateUserMutation(user=user)

class AddUserRoleMutation(graphene.Mutation):
    user = graphene.Field(UserType)
    class Arguments:
        username = graphene.String(required=True)
        role = graphene.String(required=True)

    @jwt_required
    @admin_required
    def mutate(self, info, username, role):
        user = UserModel.objects(username=username).get()
        _role = RoleModel.objects(name=role).get()
        user.roles.append(_role)
        user.save()
        return AddUserRoleMutation(user = user)
