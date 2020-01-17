from flask import g, request, jsonify
from app.common.result import trueReturn, falseReturn
from functools import wraps
import traceback

def validsign(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        if not g.user:
            response = falseReturn(None, '此操作需要登陆', 401)
            response.status_code = 401
            return response
        return func(*args, **kwargs)

    return decorator

def handle_error(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            return falseReturn(None, traceback.format_exc())
    return decorator