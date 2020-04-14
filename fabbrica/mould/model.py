import mongoengine
from mongoengine.fields import ( StringField, DecimalField, ReferenceField, IntField )
from ..part.model import PartModel
from fabbrica.company.model import CompanyModel

class MouldModel(mongoengine.Document):
    meta = {'collection': 'mould'}
    Id = StringField()
    name = StringField()
    company = ReferenceField(CompanyModel, reverse_delete_rule=mongoengine.DENY)
    part = ReferenceField(PartModel, reverse_delete_rule=mongoengine.DENY)
    cavity = IntField()
    runnerWeight = DecimalField()
