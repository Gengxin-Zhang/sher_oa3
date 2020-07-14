import datetime
import hashlib
import json
import traceback

import requests
from flask import Blueprint
from flask import current_app as flaskapp
from flask import g, jsonify, request
from mongoengine.queryset.visitor import Q

from app.api import handle_error, validsign, verify_params
from app.common.result import falseReturn, trueReturn
from app.models.User import User
from app.models.Admin import Admin
from app.models.Domain import Domain
from app.util.auth import generate_jwt, mverify_jwt
from app.util.sheet import sheet

mauth_blueprint = Blueprint('mauth', __name__, url_prefix='/masteradmin/auth')

@mauth_blueprint.before_request
def before_request():
    try:
        if request.get_data():
            g.data = request.get_json(silent=True)
        Authorization = request.headers.get('Authorization', None)
        print(Authorization)
        if Authorization:
            token = Authorization
            g.token = token
            g.user, msg = mverify_jwt(token)
        else:
            pass
    except:
        traceback.print_exc()
        return falseReturn(None, '数据错误')


@handle_error
@mauth_blueprint.route('/signin', methods=['POST'])
def signin():
    name = g.data.get("username", "").strip()
    password = g.data.get("password", "")
    user = Admin.objects(user_id=name).first()
    if not user or not user.valid_password(password):
        return falseReturn(None, "用户名或密码有误")
    return trueReturn({
        'user': user.get_base_info(),
        'token': generate_jwt(user)
    })
