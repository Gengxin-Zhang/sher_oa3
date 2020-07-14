import jwt
import time

from flask import current_app
from app.models.User import User
from app.models.Admin import Admin


def generate_jwt(user):
    token_dict = {
        'iat': time.time() + 60*60*24*30,
        'id': str(user.id)
    }
    return jwt.encode(token_dict,  # payload, 有效载体
                      current_app.config['JWT_SECRET'],  # 进行加密签名的密钥
                      algorithm="HS256",  # 指明签名算法方式, 默认也是HS256
                      ).decode()  # python3 编码后得到 bytes, 再进行解码(指明解码的格式), 得到一个str


def verify_jwt(token):
    try:
        payload = jwt.decode(token, current_app.config['JWT_SECRET'], algorithm=['HS256'])
        if payload['iat'] < time.time():
            return None, "登入超时"
        user = User.objects(id=payload['id']).first()
        if not user:
            return None, "无此用户"
        return user, ""
    except:
        return None, "数据错误"

def mverify_jwt(token):
    try:
        payload = jwt.decode(token, current_app.config['JWT_SECRET'], algorithm=['HS256'])
        if payload['iat'] < time.time():
            return None, "登入超时"
        user = Admin.objects(id=payload['id']).first()
        if not user:
            return None, "无此用户"
        return user, ""
    except:
        return None, "数据错误"