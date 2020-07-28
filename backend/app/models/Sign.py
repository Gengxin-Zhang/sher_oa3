import datetime
import hashlib
from app.models.UserBase import UserBase
from app.models.Role import Role
from app.models.User import User
from app import db

class Sign(db.Document):

    create_datetime = db.DateTimeField()  # 签到时间
    typ = db.StringField()  # 签到类型，分为'n'正常签到和's'换班签到
    week = db.IntField()  # 签到周
    user = db.ReferenceField(User,reverse_delete_rule=2)

    def create(user: User, typ: str, week: int) -> bool:
        print(user)
        last_sign = Sign.objects(user=user).order_by('create_datetime').first()
        if last_sign:
            if int(last_sign.create_datetime.timestamp() / 7200) != int(datetime.datetime.now().timestamp() / 7200):  # 卡两个小时内多次签到的情况
                s = Sign(user=user.id,create_datetime=datetime.datetime.now(),
                         typ=typ, week=week)
                last_sign = s
                s.save()
                user.save()
                return True
            else:
                return False
        else:
            s = Sign(user=user.id,create_datetime=datetime.datetime.now(),
                     typ=typ, week=week)
            last_sign = s
            s.save()
            user.save()
            return True

    def get_by_id(id):
        return Sign(id=id).first()

    def get_by_user(user:User) -> dict:
        return {"signs":[i.get_base_info() for i in Sign.objects(user=user)]}

    def get_base_info(self) -> dict:
        return {
            "id": str(self.id), 
            "create_datetime": self.create_datetime,
            "week": self.week,
            "typ": self.typ,
            "user": self.user
        }