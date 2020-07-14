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
from app.models.Role import Role
from app.models.Domain import Domain
from app.util.auth import generate_jwt, mverify_jwt
from app.util.sheet import sheet

mrole_blueprint = Blueprint('mrole', __name__, url_prefix='/masteradmin/role')

@mrole_blueprint.before_request
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
@mrole_blueprint.route('/new', methods=['POST'])
@verify_params(params=['name','permission'])
@validsign
def new_role():
    Role.new_role(g.data['name'],g.data['permission'])
    return trueReturn()

@handle_error
@mrole_blueprint.route('/remove', methods=['POST'])
@verify_params(params=['id'])
@validsign
def remove_role():
    Role.get_by_id(g.data['id']).delete()
    return trueReturn()


@handle_error
@mrole_blueprint.route('/rename', methods=['POST'])
@verify_params(params=['id','name'])
@validsign
def rename_role():
    Role.get_by_id(g.data['id']).rename(g.data['name'])
    return trueReturn()

@handle_error
@mrole_blueprint.route('/edit', methods=['POST'])
@verify_params(params=['id','permission','functions'])
@validsign
def edit_role():
    Role.get_by_id(g.data['id']).modify_permission(g.data['permission'])
    Role.get_by_id(g.data['id']).modify_functions(g.data['functions'])
    return trueReturn()


@handle_error
@mrole_blueprint.route('/ls', methods=['GET'])
@validsign
def ls_role():
    return trueReturn({"roles":[i.get_base_info() for i in Role.objects()]})