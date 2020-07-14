import datetime
import hashlib
import json
import traceback

import requests
from flask import Blueprint
from flask import current_app as flaskapp
from flask import g, jsonify, request
from mongoengine.queryset.visitor import Q

from app.api import handle_error, validsign, verify_params, validcall
from app.common.result import falseReturn, trueReturn
from app.models.User import User
from app.models.Domain import Domain
from app.models.Role import Role
from app.util.auth import generate_jwt, verify_jwt
from app.util.sheet import sheet

user_blueprint = Blueprint('user', __name__, url_prefix='/user')

@user_blueprint.before_request
def before_request():
    try:
        if request.get_data():
            g.data = request.get_json(silent=True)
        Authorization = request.headers.get('Authorization', None)
        print(Authorization)
        if Authorization:
            token = Authorization
            g.token = token
            g.user, msg = verify_jwt(token)
        else:
            pass
    except:
        traceback.print_exc()
        return falseReturn(None, '数据错误')

@handle_error
@user_blueprint.route('/new', methods=['POST'])
@verify_params(params=['name','user_id','password'])
@validsign
@validcall
def new_user():
    User.get_or_create(g.data['name'],g.data['user_id'],g.data['password'])
    return trueReturn()

@handle_error
@user_blueprint.route('/remove', methods=['POST'])
@verify_params(params=['id'])
@validsign
@validcall
def remove_user():
    u = User.get_by_id(g.data['id'])
    if not g.user.restrict_permission(u.max_permission()): 
        return falseReturn(msg='您无法删除权限不小于自己的用户')
    u.delete()
    return trueReturn()

@handle_error
@user_blueprint.route('/rename', methods=['POST'])
@verify_params(params=['id','name'])
@validsign
@validcall
def rename_user():
    u = User.get_by_id(g.data['id'])
    if not g.user.restrict_permission(u.max_permission()): 
        return falseReturn(msg='您无法重命名权限不小于自己的用户')
    u.rename(g.data['name'])
    return trueReturn()

@handle_error
@user_blueprint.route('/alloc', methods=['POST'])
@verify_params(params=['id','roles'])
@validsign
@validcall
def alloc_user():
    for i in g.data['roles']:
        if not g.user.restrict_permission(Role.get_by_id(i).permission):
            return falseReturn(msg='您无法赋予他人权限不小于自己的角色')
        if not g.user.restrict_functions(Role.get_by_id(i).allow_functions):
            return falseReturn(msg='您无法赋予他人权能不在自己范围内的角色')
    u = User.get_by_id(g.data['id'])
    u.change_role(g.data['roles'])
    return trueReturn()

@handle_error
@user_blueprint.route('/ls', methods=['GET'])
@validsign
@validcall
def ls_user():
    return trueReturn({'users':[i.get_base_info() for i in User.objects()]})

@handle_error
@user_blueprint.route('/import', methods=['POST'])
@validsign
@validcall
def import_user():
    if 'file' not in request.files:
        return falseReturn(None, '无文件')
    f = request.files['file']
    if f.filename == '':
        return falseReturn(None, '未选择上传')
    else:
        sheet(f)
        return trueReturn()
