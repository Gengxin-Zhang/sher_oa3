from app import db
from app.models.User import User
from app.models.UserBase import UserBase

class Domain(UserBase):

    members = db.ListField(db.ReferenceField(User,reverse_delete_rule=4))
    monitors = db.ListField(db.ReferenceField(User,reverse_delete_rule=4))


    def new_domain(name,owner:User): # 超管新建悬空域不走这里
        if owner:
            return Domain(name=name,members=[owner],monitors=[owner]).save()
        else:
            return Domain(name=name).save()

    def insert_members(self,member_list):
        for _ in member_list:
            if not isinstance(_,UserBase):
                _ = UserBase.get_by_id(_)
            self.update(add_to_set__members=_)
        return self

    def delete_members(self,member_list):
        for _ in member_list:
            self.update(pull__members=_)
        return self

    def modify_members(self,members,monitors):
        for p,i in enumerate(members):
            if not isinstance(i,UserBase):
                members[p] = UserBase.get_by_id(i)
        for p,i in enumerate(monitors):
            if not isinstance(i,UserBase):
                monitors[p] = UserBase.get_by_id(i)
        self.member = members
        self.monitors = monitors

    def get_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "monitors": self.monitors,
            "last_modify": self.last_modify,
            "create_datetime": self.create_datetime,
            "members":self.members
        }
