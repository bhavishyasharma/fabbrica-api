import mongoengine
from mongoengine.fields import ( StringField, DecimalField, ReferenceField, IntField )
from fabbrica.company.model import CompanyModel

class MachineModel(mongoengine.Document):
    meta = {'collection': 'machine'}
    Id = StringField()
    name = StringField()
    make = StringField()
    model = StringField()
    company = ReferenceField(CompanyModel, reverse_delete_rule=mongoengine.DENY)
    clampingCapacity = IntField()
    injectionVolume = DecimalField()
