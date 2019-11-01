from flask import g, jsonify, Blueprint, request
from flask import current_app as flaskapp
from app.util.common import trueReturn, falseReturn
from app.util.auth import generate_jwt, verify_jwt
from app.models.User import User
from mongoengine.queryset.visitor import Q
import requests
import json
import hashlib
import datetime

import traceback
auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@auth_blueprint.before_request
def before_request():
    try:
        if request.get_data():
            g.data = request.get_json(silent=True)
        Authorization = request.headers.get('Authorization', None)
        if Authorization:
            typ, token = Authorization.split()
            if typ == 'token':
                g.token = token
                g.user, msg = verify_jwt(token)
        else:
            pass
    except:
        traceback.print_exc()
        return falseReturn(None, '数据错误')


def str2md5(str):
    return hashlib.md5(hashlib.md5(str.encode('utf-8')).hexdigest().encode('utf-8')).hexdigest()


@auth_blueprint.route('/signin', methods=['POST'])
def signin():
    try:
        name = g.data.get("name")
        password = g.data.get("password")
        user = User.objects(user_id=name).first()
        if not user:
            return falseReturn(None, "用户不存在")
        if not user.password == str2md5(password):
            return falseReturn(None, "用户名或密码不存在")
        return trueReturn({
            'userData': {
                'id': str(user.id),
                'name': user.name,
                'token': generate_jwt(user),
                'user_id': user.user_id,
                'permission': user.permission
            }
        })
    except:
        return falseReturn(None, "")


@auth_blueprint.route('/verify', methods=['GET'])
def verify():
    try:
        return trueReturn({'userData': {
            'id': str(g.user.id),
            'name': g.user.name,
            'token': g.token,
            'user_id': g.user.user_id,
            'permission': g.user.permission
        }}, "")
    except:
        traceback.print_exc()
        return falseReturn()
