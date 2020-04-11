import graphene
from flask_jwt_extended import ( jwt_required )
from .type import PartType
from .model import PartModel

class AddPartMutation(graphene.Mutation):
    part = graphene.Field(PartType)

    class Arguments:
        name = graphene.String(required=True)
        material = graphene.String(required=True)
        color = graphene.String(required=False)
        weight = graphene.Decimal(required=True)

    @jwt_required
    def mutate(self, info, name, material, weight, color=None):
        part = PartModel(
            name = name,
            material = material,
            color = color,
            weight = weight
        )
        part.save()
        return AddPartMutation(part=part)