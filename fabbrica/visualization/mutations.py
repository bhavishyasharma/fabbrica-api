import graphene
from flask_jwt_extended import ( jwt_required )
from .type import VisualizationType
from .model import VisualizationModel


class AddVisualizationMutation(graphene.Mutation):
    visualization = graphene.Field(VisualizationType)

    class Arguments:
        name = graphene.String(required=True)
        parentType = graphene.String(required=True)
        visualizationType = graphene.String(required=True)
        query = graphene.String(required=True)
        parameters = graphene.List(graphene.String, required=True)
        width = graphene.Int(required=False)

    @jwt_required
    def mutate(self, info, name, parentType, visualizationType, query, parameters, width):
        visualization = VisualizationModel(
            name = name,
            parentType = parentType,
            visualizationType = visualizationType,
            query = query,
            parameters = parameters,
            width = width
        )
        visualization.save()
        return AddVisualizationMutation(visualization=visualization)

class UpdateVisualizationMutation(graphene.Mutation):
    visualization = graphene.Field(VisualizationType)

    class Arguments:
        visualizationId = graphene.String(required=True)
        name = graphene.String()
        parentType = graphene.String()
        visualizationType = graphene.String()
        query = graphene.String()
        parameters = graphene.List(graphene.String)
        width = graphene.Int()

    @jwt_required
    def mutate(self, info, visualizationId, name=None, parentType=None, visualizationType=None, query=None, parameters=None, width=None):
        visualization = VisualizationModel.objects(id=visualizationId).get()
        print(parameters)
        if name is not None:
            visualization.name = name
        if parentType is not None:
            visualization.parentType = parentType
        if visualizationType is not None:
            visualization.visualizationType = visualizationType
        if query is not None:
            visualization.query = query
        if parameters is not None:
            visualization.parameters = parameters
        if width is not None:
            visualization.width = width
        visualization.save()
        return UpdateVisualizationMutation(visualization=visualization)