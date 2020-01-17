from flask import jsonify,request,Response
def trueReturn(data=None, msg="", code=0):
    return jsonify({
        'data': data,
        'msg': msg,
        'status': True
    })

def falseReturn(data=None, msg="", code=0):
    return jsonify({
        'data': data,
        'msg': msg,
        'status': False
    })