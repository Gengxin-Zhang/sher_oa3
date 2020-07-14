import datetime
import hashlib
from app.models.UserBase import UserBase
from app import db


def str2md5(str):
    return hashlib.sha256(hashlib.sha256(str.encode('utf-8')).hexdigest().encode('utf-8')).hexdigest()


class Role(db.Document):
    permission = db.IntField()
    name = db.StringField()
    allow_functions = db.ListField(db.StringField(),default=[])

    def new_role(name,permission):
        return Role(name=name,permission=permission).save()

    def get_by_id(id):
        return Role.objects(id=id).first()

    def rename(self,name):
        self.name = name
        return self.save()

    def modify_permission(self, permission):
        self.permission = permission
        return self.save()

    def modify_functions(self,functions):
        self.allow_functions = functions
        return self.save()

    def get_base_info(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "permission": self.permission,
            "allow_functions":self.allow_functions
        }



