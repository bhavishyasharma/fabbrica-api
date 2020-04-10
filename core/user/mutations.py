import graphene
from .type import UserType, UserInput
from .model import UserModel
from ..role.model import RoleModel


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
            roles = [userRole._id]
        )
        user.setPassword(user_data.password)
        user.save()
        return RegisterUserMutation(user=user)

class AddUserRoleMutation(graphene.Mutation):
    user = graphene.Field(UserType)
    class Arguments:
        username = graphene.String(required=True)
        role = graphene.String(required=True)

    def mutate(self, info, username, role):
        user = UserModel.objects(username=username).get()
        _role = RoleModel.objects(name=role).get()
        user.roles.append(_role)
        user.save()
        return AddUserRoleMutation(user = user)
