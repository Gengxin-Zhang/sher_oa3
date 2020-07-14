import re
import os

ignore = { 
    'initialize.py',
    '替换为管理专用用.py',
    '__init__.py',
    'auth.py',
    'domain.py',
    'role.py',
    'user.py'
}

for _ in os.listdir():
    if _ not in ignore and _[-3:]=='.py':
        with open(_,'r',encoding='utf-8') as f:
            s = f.read()
        __ = _[:-3]
        s=s.replace(__,'m'+__)
        s=s.replace('verify_jwt','mverify_jwt')
        s=s.replace('@validcall\n','')
        with open('masteradmin/'+_,'w',encoding='utf-8') as f:
            f.write(s)


# ============Caution=============
"""
from flask_mongoengine import MongoEngine

db = MongoEngine()

db.connect('xiajibagao')

class User(db.Document):
    name = db.StringField()
    a = db.StringField()

class t(db.Document):
    uu = db.ListField(db.ReferenceField(User,reverse_delete_rule=4))

class c(db.Document):
    uu = db.ReferenceField(User,reverse_delete_rule=1)

u1 = User(name='1').save()
u2 = User(name='2').save()

s = t(uu=[]).save()
ss = t(uu=[u2]).save()
sss = t(uu=[u2,u1]).save()

User.objects(name='2').first().delete()



for i in t.objects():
    i.delete()

for i in User.objects():
    i.delete()

for i in c.objects():
    i.delete()
"""