from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
# from flask_wtf.csrf import CsrfProtect
from flask_moment import Moment
from config import Config


db = SQLAlchemy()
bootstrap = Bootstrap()
moment = Moment()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)
    # CsrfProtect(app)

    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)

    from .main import main
    app.register_blueprint(main)

    from .admin import admin
    app.register_blueprint(admin, url_prefix='/admin')

    from .auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    return app
