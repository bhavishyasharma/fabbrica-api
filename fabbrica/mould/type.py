import graphene
from graphene_mongo import MongoengineObjectType
from .model import MouldModel

class MouldType(MongoengineObjectType, graphene.ObjectType):
    class Meta:
        model = MouldModel

class MouldVisualizationType(graphene.ObjectType):
    time = graphene.String()
    cycle_time = graphene.Float()
    power_consumption = graphene.Float()

    def resolve_time(parent, info):
        return parent['time']

    def resolve_cycle_time(parent, info):
        return parent['cycleTime']

    def resolve_power_consumption(parent, info):
        return parent['powerConsumption']
    
    