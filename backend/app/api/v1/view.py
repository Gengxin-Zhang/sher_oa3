import time
import datetime
import json
import os
import sys

from flask import jsonify, g, request, Blueprint
# from app.models import User
from app.common import trueReturn, falseReturn

api_v1 = Blueprint('api_v1', __name__)

@api_v1.before_request
def before_request():
    try:
        user = get_user
        if not user:
            return jsonify(falseReturn(None, '没有权限'))
        g.user = user
    except:
        return jsonify(falseReturn(None, '出现错误'))

def get_user(data):
    try:
        key = data.get('key', '')
    except:
        return None