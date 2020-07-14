import datetime
import hashlib
import json
import traceback
import os

import requests
from flask import Blueprint
from flask import current_app as flaskapp
from flask import g, jsonify, request
from mongoengine.queryset.visitor import Q

from app.api import handle_error, validsign, verify_params
from app.common.result import falseReturn, trueReturn
from app.models.User import User
from app.models.Domain import Domain
from app.models.Admin import Admin
from app.models.Role import Role

from app import db

initialize_blueprint = Blueprint('initialize', __name__, url_prefix='/initialize')


@initialize_blueprint.before_request
def before_request():
    try:
        if os.path.exists('isinit.flag'):
            return falseReturn(msg="拒绝访问：已经初始化过")
        if request.get_data():
            g.data = request.get_json(silent=True)
    except:
        traceback.print_exc()
        return falseReturn(None, '数据错误')


@handle_error
@initialize_blueprint.route('/exec', methods=['POST'])
@verify_params(params=['user','password'])
def initialize_instance():
    Admin.insert_admin(g.data['user'],g.data['password'])
    Domain(name='默认部员域').save()
    Role.new_role('成员',0)
    Role.new_role('部长',64,['new_user','remove_user','rename_user','alloc_user','ls_user','import_from_sheet'])
    Role.new_role('总监',4096,['*'])
    with open('isinit.flag','w') as f:
        pass
    return trueReturn(msg="初始化完成")