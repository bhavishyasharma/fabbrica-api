import graphene
from graphene_mongo import MongoengineObjectType
from .model import VisualizationModel

class VisualizationType(MongoengineObjectType, graphene.ObjectType):
    class Meta:
        model = VisualizationModel

class VisualizationResponse(graphene.ObjectType):
    data = graphene.types.json.JSONString()
    visualization_type = graphene.String()