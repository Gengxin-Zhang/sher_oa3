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
from app.models.Domain import Domain
from app.models.Role import Role
from app.util.auth import generate_jwt, mverify_jwt
from app.util.sheet import sheet

muser_blueprint = Blueprint('muser', __name__, url_prefix='/masteradmin/user')

@muser_blueprint.before_request
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
@muser_blueprint.route('/new', methods=['POST'])
@verify_params(params=['name','user_id','password'])
@validsign
def new_user():
    User.get_or_create(g.data['name'],g.data['user_id'],g.data['password'])
    return trueReturn()

@handle_error
@muser_blueprint.route('/remove', methods=['POST'])
@verify_params(params=['id'])
@validsign
def remove_user():
    User.get_by_id(g.data['id']).delete()
    return trueReturn()

@handle_error
@muser_blueprint.route('/rename', methods=['POST'])
@verify_params(params=['id','name'])
@validsign
def rename_user():
    User.get_by_id(g.data['id']).rename(g.data['name'])
    return trueReturn()

@handle_error
@muser_blueprint.route('/alloc', methods=['POST'])
@verify_params(params=['id','roles'])
@validsign
def alloc_user():
    u = User.get_by_id(g.data['id'])
    u.change_role(g.data['roles'])
    return trueReturn()

@handle_error
@muser_blueprint.route('/ls', methods=['GET'])
@validsign
def ls_user():
    return trueReturn({'users':[i.get_base_info() for i in User.objects()]})

@handle_error
@muser_blueprint.route('/import', methods=['POST'])
@validsign
def import_user():
    if 'file' not in request.files:
        return falseReturn(None, '无文件')
    f = request.files['file']
    if f.filename == '':
        return falseReturn(None, '未选择上传')
    else:
        sheet(f)
        return trueReturn()
