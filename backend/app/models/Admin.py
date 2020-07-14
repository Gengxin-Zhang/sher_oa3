import datetime
import hashlib
from app import db

def str2md5(str):
    return hashlib.sha256(hashlib.sha256(str.encode('utf-8')).hexdigest().encode('utf-8')).hexdigest()


class Admin(db.Document):
    user_id = db.StringField()
    password = db.StringField()
    last_modify = db.DateTimeField()
    create_datetime = db.DateTimeField()
    server_starttime = db.DateTimeField() # 服务器开始运行的时间，后面用于判断签到周

    def insert_admin(user_id, password): # 原则上只用一次
        return Admin(user_id=user_id, 
                    password=str2md5(password),
                    create_datetime=datetime.datetime.now(),
                    server_starttime=datetime.datetime.now(),
                    last_modify=datetime.datetime.now()).save()

    def set_password(self, password):
        self.password = str2md5(password)
        self.last_modify = datetime.datetime.now()
        return self.save()

    def valid_password(self, password):
        return self.password == str2md5(password)

    def change_starttime(self,t): # 记得做这个接口
        self.server_starttime = t
        self.last_modify = datetime.datetime.now()
        return self.save()

    def get_base_info(self):
        return {
            "id": str(self.id),
            "user_id": self.user_id,
            "last_modify": self.last_modify,
            "create_datetime": self.create_datetime,
            "server_starttime" : self.server_starttime
        }