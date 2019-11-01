from flask import jsonify
def trueReturn(data, msg=""):
    return jsonify({
        'data': data,
        'msg': msg,
        'status': True
    })

def falseReturn(data=None, msg=""):
    return jsonify({
        'data': data,
        'msg': msg,
        'status': False
    })