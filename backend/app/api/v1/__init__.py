from flask import g, request, jsonify
from app.util.common import trueReturn, falseReturn


def validsign(func):
    def decorator():
        if not g.user:
            return jsonify(falseReturn(None, '此操作需要登陆'))
        return func()

    return decorator
