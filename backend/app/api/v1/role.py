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
from app.models.Role import Role
from app.models.Domain import Domain
from app.util.auth import generate_jwt, verify_jwt
from app.util.sheet import sheet

role_blueprint = Blueprint('role', __name__, url_prefix='/role')

@role_blueprint.before_request
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
@role_blueprint.route('/new', methods=['POST'])
@verify_params(params=['name','permission'])
@validsign
@validcall
def new_role():
    if g.user.restrict_permission(g.data['permission']):
        Role.new_role(g.data['name'],g.data['permission'])
        return trueReturn()
    else:
        return falseReturn(msg='您无法新建权限不小于自己的角色')

@handle_error
@role_blueprint.route('/remove', methods=['POST'])
@verify_params(params=['id'])
@validsign
@validcall
def remove_role():
    if g.user.restrict_permission(Role.get_by_id(g.data['id']).permission):
        if g.user.restrict_functions(Role.get_by_id(g.data['id']).allow_functions):
            Role.get_by_id(g.data['id']).delete()
            return trueReturn()
        else:
            return falseReturn(msg='您无法删除权能比自己多的角色')
    else:
        return falseReturn(msg='您无法删除权限不小于自己的角色')

@handle_error
@role_blueprint.route('/rename', methods=['POST'])
@verify_params(params=['id','name'])
@validsign
@validcall
def rename_role():
    if g.user.restrict_permission(Role.get_by_id(g.data['id']).permission):
        if g.user.restrict_functions(Role.get_by_id(g.data['id']).allow_functions):
            Role.get_by_id(g.data['id']).rename(g.data['name'])
            return trueReturn()
        else:
            return falseReturn(msg='您无法为权能比自己多的角色更名')
    else:
        return falseReturn(msg='您无法为权限不小于自己的角色更名')

@handle_error
@role_blueprint.route('/edit', methods=['POST'])
@verify_params(params=['id','permission','functions'])
@validsign
@validcall
def edit_role():
    if g.user.restrict_permission(g.data['permission']):
        if g.user.restrict_functions(g.data['functions']):
            Role.get_by_id(g.data['id']).modify_permission(g.data['permission'])
            Role.get_by_id(g.data['id']).modify_functions(g.data['functions'])
            return trueReturn()
        else:
            return falseReturn(msg='您无法为角色分配自己没有的权能')
    else:
        return falseReturn(msg='您无法为角色分配不小于自身的权限')


@handle_error
@role_blueprint.route('/ls', methods=['GET'])
@validsign
@validcall
def ls_role():
    return trueReturn({"roles":[i.get_base_info() for i in Role.objects()]})