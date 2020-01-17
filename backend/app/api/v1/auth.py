import datetime
import hashlib
import json
import traceback

import requests
from flask import Blueprint
from flask import current_app as flaskapp
from flask import g, jsonify, request
from mongoengine.queryset.visitor import Q

from app.api import handle_error, validsign
from app.common.result import falseReturn, trueReturn
from app.models.User import User
from app.util.auth import generate_jwt, verify_jwt

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@auth_blueprint.before_request
def before_request():
    try:
        if request.get_data():
            g.data = request.get_json(silent=True)
        Authorization = request.headers.get('Authorization', None)
        print(Authorization)
        if Authorization:
            typ, token = Authorization.split()
            if typ == 'Bearer':
                g.token = token
                g.user, msg = verify_jwt(token)
        else:
            pass
    except:
        traceback.print_exc()
        return falseReturn(None, '数据错误')


@handle_error
@auth_blueprint.route('/signin', methods=['POST'])
def signin():
    name = g.data.get("username", "").strip()
    password = g.data.get("password", "")
    user = User.objects(user_id=name).first()
    if not user or not user.valid_password(password):
        return falseReturn(None, "用户名或密码有误")
    return trueReturn({
        'user': user.get_base_info(),
        'token': generate_jwt(user),
    })


@handle_error
@auth_blueprint.route('/valid_token', methods=['POST'])
@validsign
def verify():
    return trueReturn({'user': g.user.get_base_info()}, "")

