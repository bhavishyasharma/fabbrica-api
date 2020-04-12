from mongoengine.errors import DoesNotExist
from core.role.model import RoleModel
from core.user.model import UserModel
from fabbrica.acl.model import AclModel

def init_db():
    try:
        admin = RoleModel.objects(name="admin").get()
    except DoesNotExist:
        admin = RoleModel(name="admin", label="Administrator")
        admin.save()

    try:
        consumer = RoleModel.objects(name="consumer").get()
    except DoesNotExist:
        consumer = RoleModel(name="consumer", label="Consumer")
        consumer.save()

    try:
        user = RoleModel.objects(name="user").get()
    except DoesNotExist:
        user = RoleModel(name="user", label="User")
        user.save()

    try:
        UserModel.objects(username="administrator").get()
    except DoesNotExist:
        adminUser = UserModel(firstname="Bhavishya", lastname="Sharma",
            username="administrator", email="admin@futech.co.in")
        adminUser.setPassword("Bbs199509")
        adminUser.save()
        UserModel.objects(id=adminUser.id).update_one(push__roles=admin)

    try:
        UserModel.objects(username="telegraf").get()
    except DoesNotExist:
        telegrafUser = UserModel(firstname="telegraf", lastname="user",
            username="telegraf", email="telegraf@futech.co.in")
        telegrafUser.setPassword("telegraf")
        telegrafUser.save()
        UserModel.objects(id=telegrafUser.id).update_one(push__roles=consumer)

    try:
        AclModel.objects(username="telegraf", clientid="telegraf", publish="#").get()
    except DoesNotExist:
        acl = AclModel(username="telegraf", clientid="telegraf", publish=["#"], subscribe=[""], pubsub=[""])
        acl.save()

    