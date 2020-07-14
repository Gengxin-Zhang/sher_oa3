from app import db
import datetime

class UserBase(db.Document):
    name = db.StringField()
    last_modify = db.DateTimeField()
    create_datetime = db.DateTimeField()
    meta = {'allow_inheritance': True}

    def rename(self,new_name):
        self.name = new_name
        self.last_modify = datetime.datetime.now()
        return self.save()

    def get_by_id(id):
        return UserBase.objects(id=id).first()

    def get_base_info(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "last_modify": self.last_modify,
            "create_datetime": self.create_datetime
        }



