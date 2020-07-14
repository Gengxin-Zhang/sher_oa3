import datetime
import os
import sys
import time

from flask import Flask, current_app, g
from flask_cors import CORS
from flask_mongoengine import MongoEngine


db = MongoEngine()

def create_app() -> Flask:
    flask_app = Flask(__name__)
    # 加载配置
    from app.config import get_config
    _get_config = get_config()
    flask_app.config.from_object(_get_config)

    # 添加上下文
    ctx = flask_app.app_context()
    ctx.push()
    # 添加跨域
    CORS(flask_app, support_credentials=True)

    # 初始化数据库
    db.init_app(flask_app)

    # 分配路由
    from app.util.GreenPrint import GreenPrint
    from app.api.v1.auth import auth_blueprint
    from app.api.v1.domain import domain_blueprint
    from app.api.v1.user import user_blueprint
    from app.api.v1.role import role_blueprint
    from app.api.v1.event import event_blueprint
    from app.api.v1.routine import routine_blueprint
    from app.api.v1.sign import sign_blueprint
    from app.api.v1.initialize import initialize_blueprint

    from app.api.v1.masteradmin.auth import mauth_blueprint
    from app.api.v1.masteradmin.domain import mdomain_blueprint
    from app.api.v1.masteradmin.user import muser_blueprint
    from app.api.v1.masteradmin.role import mrole_blueprint
    from app.api.v1.masteradmin.event import mevent_blueprint
    from app.api.v1.masteradmin.routine import mroutine_blueprint
    from app.api.v1.masteradmin.sign import msign_blueprint
    # from app.api.v1.sign import sign
    # from app.api.v1.base_info import base_info
    # from app.api.v1.domain import domain
    api_v1 = GreenPrint('api', __name__, url_prefix='/api/v1')
    api_v1.register_blueprint(auth_blueprint)
    api_v1.register_blueprint(domain_blueprint)
    api_v1.register_blueprint(user_blueprint)
    api_v1.register_blueprint(role_blueprint)
    api_v1.register_blueprint(event_blueprint)
    api_v1.register_blueprint(routine_blueprint)
    api_v1.register_blueprint(sign_blueprint)
    api_v1.register_blueprint(initialize_blueprint)

    api_v1.register_blueprint(mauth_blueprint)
    api_v1.register_blueprint(mdomain_blueprint)
    api_v1.register_blueprint(muser_blueprint)
    api_v1.register_blueprint(mrole_blueprint)
    api_v1.register_blueprint(mevent_blueprint)
    api_v1.register_blueprint(mroutine_blueprint)
    api_v1.register_blueprint(msign_blueprint)
    
    
    # api_v1.register_blueprint(base_info)
    # api_v1.register_blueprint(domain)

    flask_app.register_blueprint(api_v1)

    return flask_app
