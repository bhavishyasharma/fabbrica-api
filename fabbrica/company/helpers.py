from mongoengine.errors import DoesNotExist
from .model import CompanyModel
from fabbrica.acl.model import AclModel
from fabbrica.machine.model import MachineModel

def updateAcl(company:CompanyModel):
    machines = MachineModel.objects(company=company).all()
    for machine in machines:
        for user in company.users:
            try:
                acl = AclModel.objects(clientid=str(machine.id),username=user.username, publish=str(machine.id)).get()
            except DoesNotExist:
                acl = AclModel(username=user.username, clientid=str(machine.id), publish=[str(machine.id)], subscribe=[""], pubsub=["#"])
                acl.save()

