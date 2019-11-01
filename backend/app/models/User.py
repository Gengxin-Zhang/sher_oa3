from app import db
import datetime


class User(db.Document):
    name = db.StringField()
    permission = db.IntField(default=0)
    contribution = db.IntField(default=0)
    user_id = db.StringField()
    bio = db.StringField()
    avatar = db.StringField()
    banner = db.StringField()
    last_modify = db.DateTimeField()
    create_datetime = db.DateTimeField(default=datetime.datetime.now())
    password = db.StringField()
    status = db.StringField(default='p') # p: 一切正常; f: 被ban了; 