import graphene
from flask_jwt_extended import (jwt_required)
from flask_influxdb import InfluxDB
from core.common.type import Filter, Pagination
from core.common.helpers import filter_qs, pagination_qs, sortings_qs
from .type import MouldType, MouldVisualizationType
from .model import MouldModel
from .mutations import AddMouldMutation, UpdateMouldMutation

class Query(graphene.ObjectType):
    moulds = graphene.List(MouldType, filters=graphene.List(Filter, required=False), 
        pagination=Pagination(required=False), sortings = graphene.List(graphene.String, required=False))
    mould = graphene.Field(MouldType, mouldId=graphene.String(required=True))
    mould_visualization = graphene.List(MouldVisualizationType, mouldId=graphene.String(required=True), interval=graphene.String(required=False), fromTime=graphene.types.datetime.DateTime(required=True), toTime=graphene.types.datetime.DateTime(required=True))
    
    @jwt_required
    def resolve_moulds(self, info, filters=None, pagination=None, sortings=None):
        qs = MouldModel.objects()
        qs = filter_qs(qs, filters)
        qs = pagination_qs(qs, pagination)
        qs = sortings_qs(qs, sortings)
        return list(MouldModel.objects().all())
    
    def resolve_mould(self, info, mouldId=None):
        mould = MouldModel.objects(id=mouldId).get()
        return mould

    def resolve_mould_visualization(self, info, mouldId=None, fromTime=None, toTime=None, interval="20s"):
        influx = InfluxDB()
        query = 'SELECT mean("cycleTime") AS "cycleTime", sum("powerConsumption") AS "powerConsumption" FROM "mqtt_consumer" WHERE time > \'{fromTime}\' AND time < \'{toTime}\' AND "mouldId"=\'{mouldId}\' GROUP BY time({interval}) FILL(0)'.format(mouldId=mouldId, fromTime=fromTime.isoformat(), toTime=toTime.isoformat(), interval=interval)
        result = influx.query(query)
        return list(result.get_points(measurement='mqtt_consumer', tags=None))

class Mutation(graphene.ObjectType):
    add_mould = AddMouldMutation.Field()
    update_mould = UpdateMouldMutation.Field()

schema = graphene.Schema(query=Query, types=[MouldType], mutation=Mutation)