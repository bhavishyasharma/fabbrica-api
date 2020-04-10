import graphene
from .type import RoleType, AddRoleInput
from .model import RoleModel


class AddRoleMutation(graphene.Mutation):
    role = graphene.Field(RoleType)

    class Arguments:
        role_data = AddRoleInput(required=True)

    def mutate(self, info, role_data=None):
        role = RoleModel(
            name = role_data.name,
        )
        role.save()
        return AddRoleMutation(role=role)
