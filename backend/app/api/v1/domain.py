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
from app.util.auth import generate_jwt, verify_jwt
from app.util.sheet import sheet

domain_blueprint = Blueprint('domain', __name__, url_prefix='/domain')


@domain_blueprint.before_request
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
@domain_blueprint.route('/new', methods=['POST'])
@verify_params(params=['name'])
@validsign
def new_domain():
    Domain.new_domain(g.data['name'],g.user)
    return trueReturn()

@handle_error
@domain_blueprint.route('/remove', methods=['POST'])
@verify_params(params=['id'])
@validsign
def remove_domain():
    d = Domain.get_by_id(g.data['id'])
    if g.user in d.monitors:
        d.delete()
        return trueReturn()
    else:
        return falseReturn(msg='您没有此域的删除权限')

@handle_error
@domain_blueprint.route('/rename', methods=['POST'])
@verify_params(params=['id','name'])
@validsign
def rename_domain():
    d = Domain.get_by_id(g.data['id'])
    if g.user in d.monitors:
        d.rename(g.data['name'])
        return trueReturn()
    else:
        return falseReturn(msg='您没有此域的更名权限')

@handle_error
@domain_blueprint.route('/edit', methods=['POST'])
@verify_params(params=['id','members','monitors'])
@validsign
def edit_domain():
    d = Domain.get_by_id(g.data['id'])
    if g.user in d.monitors:
        d.modify_members(g.data['members'],g.data['monitors'])
        return trueReturn()
    else:
        return falseReturn(msg='您没有此域的管理权限')

@handle_error
@domain_blueprint.route('/ls', methods=['GET'])
@validsign
def ls_domain():
    data = {'monitors':[],'members':[]}
    for i in Domain.objects(monitors__in=[g.user]):
        data['monitors'].append(i.get_json())
    for i in Domain.objects(members__in=[g.user]):
        data['members'].append(i.get_json())
    return trueReturn(data)

@handle_error
@domain_blueprint.route('/show', methods=['GET'])
@validsign
@validcall
def show_all_domain():
    return trueReturn({"domains":[i.get_json() for i in Domain.objects()]})