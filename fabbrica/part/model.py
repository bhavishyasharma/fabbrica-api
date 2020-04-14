import mongoengine
from mongoengine.fields import ( StringField, DecimalField, ReferenceField )
from fabbrica.company.model import CompanyModel

class PartModel(mongoengine.Document):
    meta = {'collection': 'part'}
    Id = StringField()
    name = StringField()
    company = ReferenceField(CompanyModel, reverse_delete_rule=mongoengine.DENY)
    material = StringField()
    color = StringField(required=False)
    weight = DecimalField()
