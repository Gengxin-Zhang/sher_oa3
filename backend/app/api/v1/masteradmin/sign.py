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
from app.models.Sign import Sign
from app.models.Domain import Domain
from app.models.Admin import Admin
from app.models.Routine import Routine
from app.models.Role import Role
from app.util.auth import generate_jwt, mverify_jwt
from app.util.sheet import sheet

msign_blueprint = Blueprint('msign', __name__, url_prefix='/masteradmin/sign')

time_table = {
    0: range(28800, 36000),
    1: range(36000, 43200),
    2: range(50400, 57600),
    3: range(57600, 64800),
    4: range(68400, 75600)
}


@msign_blueprint.before_request
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
@msign_blueprint.route('/export', methods=['GET'])
@validsign
def export_sign():
    return trueReturn({'all_signs': [{'user': j, 'signs': [i.get_base_info() for i in Sign.objects(user=j)]} for j in User.objects()]})
