import graphene
from flask_jwt_extended import (jwt_required)
from core.common.type import Filter, Pagination
from core.common.helpers import filter_qs, pagination_qs, sortings_qs
from .type import VisualizationType
from .model import VisualizationModel
from .mutations import AddVisualizationMutation, UpdateVisualizationMutation

class Query(graphene.ObjectType):
    visualizations = graphene.List(VisualizationType, filters=graphene.List(Filter, required=False), 
        pagination=Pagination(required=False), sortings = graphene.List(graphene.String, required=False))
    visualization = graphene.Field(VisualizationType, visualizationId=graphene.String(required=True))
    
    @jwt_required
    def resolve_visualizations(self, info, filters=None, pagination=None, sortings=None):
        qs = VisualizationModel.objects()
        qs = filter_qs(qs, filters)
        qs = pagination_qs(qs, pagination)
        qs = sortings_qs(qs, sortings)
        return list(VisualizationModel.objects().all())

    def resolve_visualization(self, info, visualizationId=None):
        visualization = VisualizationModel.objects(id=visualizationId).get()
        return visualization

class Mutation(graphene.ObjectType):
    add_visualization = AddVisualizationMutation.Field()
    update_visualization = UpdateVisualizationMutation.Field()

schema = graphene.Schema(query=Query, types=[VisualizationType], mutation=Mutation)