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

def validcall(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        for i in g.user.roles:
            if func.__name__ in i.allow_functions or i.allow_functions == ['*']: # 懒人标记*
                return func(*args, **kwargs)
        return falseReturn(None, f'没有使用{func.__name__}的权限', 401)
    return decorator

def handle_error(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            return falseReturn(None, traceback.format_exc())
    return decorator

def smart_decorator(decorator):

    def decorator_proxy(func=None, **kwargs):
        if func is not None:
            return decorator(func=func, **kwargs)

        def decorator_proxy(func):
            return decorator(func=func, **kwargs)

        return decorator_proxy

    return decorator_proxy

@smart_decorator
def verify_params(func, params=[]):
    @wraps(func)
    def decorator(*args, **kwargs):
        for param in params:
            if not g.data or not param in g.data:
                return falseReturn(None, "缺少参数:{}".format(param))
        return func(*args, **kwargs)
    return decorator
