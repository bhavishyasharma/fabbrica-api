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

class UpdatePartMutation(graphene.Mutation):
    part = graphene.Field(PartType)

    class Arguments:
        partId = graphene.String(required=True)
        name = graphene.String()
        material = graphene.String()
        color = graphene.String()
        weight = graphene.Decimal()

    @jwt_required
    def mutate(self, info, partId, name=None, material=None, color=None, weight=None):
        part = PartModel.objects(id=partId).get()
        if name is not None:
            part.name = name
        if material is not None:
            part.material = material
        if color is not None:
            part.color = color
        if weight is not None:
            part.weight = weight
        part.save()
        return UpdatePartMutation(part=part)