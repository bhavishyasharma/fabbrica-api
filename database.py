from mongoengine.errors import DoesNotExist
from core.role.model import RoleModel
from core.user.model import UserModel

def init_db():
    try:
        admin = RoleModel.objects(name="admin").get()
    except DoesNotExist:
        admin = RoleModel(name="admin", label="Administrator")
        admin.save()

    try:
        user = RoleModel.objects(name="user").get()
    except DoesNotExist:
        user = RoleModel(name="user", label="User")
        user.save()

    try:
        UserModel.objects(username="administrator").get()
    except DoesNotExist:
        adminUser = UserModel(firstname="Bhavishya", lastname="Sharma",
            username="administrator", email="admin@futech.co.in",
            roles = [admin._id, user._id])
        adminUser.setPassword("Bbs199509")
        adminUser.save()