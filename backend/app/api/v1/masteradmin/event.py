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
from app.models.Event import Event
from app.models.Routine import Routine
from app.models.Role import Role
from app.util.auth import generate_jwt, mverify_jwt
from app.util.sheet import sheet

mevent_blueprint = Blueprint('mevent', __name__, url_prefix='/mevent')

@mevent_blueprint.before_request
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
@mevent_blueprint.route('/new', methods=['POST'])
@verify_params(params=['name','frequency','offset','start','end','timenode'])
@validsign
def new_mevent(): 
    Event.new_event(
        g.user,
        g.data['name'],
        g.data['frequency'],
        g.data['offset'],
        g.data['start'],
        g.data['end'],
        g.data['timenode']
    )
    return trueReturn()

@handle_error
@mevent_blueprint.route('/edit', methods=['POST'])
@verify_params(params=['id','name','frequency','offset','start','end','timenode'])
@validsign
def edit_event():
    e = Event.get_by_id(g.data['id'])
    e.edit_event(
        g.user,
        g.data['name'],
        g.data['frequency'],
        g.data['offset'],
        g.data['start'],
        g.data['end'],
        g.data['timenode']
    )
    return trueReturn()

@handle_error
@mevent_blueprint.route('/remove', methods=['POST'])
@verify_params(params=['id'])
@validsign
def remove_event():
    e = Event.get_by_id(g.data['id'])
    e.delete()
    return trueReturn()