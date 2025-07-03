from flask import Flask

from src.app.config import Config
from src.app.extensions import db


def create_app():
    app = Flask(__name__)

    #添加配置
    app.config.from_object(Config)

    # 初始化扩展
    db.init_app(app)

    # 注册蓝图
    from src.bps.PickerRouter import picker_bp
    app.register_blueprint(picker_bp,url_prefix='/picker')

    # 添加初始路由
    @app.route('/')
    def hello_world():
        return 'Hello World!'

    return app
