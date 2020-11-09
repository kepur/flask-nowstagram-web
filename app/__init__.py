from flask import Flask
from flask import blueprints
from flask_login import LoginManager
login_manager=LoginManager()
login_manager.login_view='/regloginpage/'

def create_app():
    app=Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    from app.admin.models import db
    db.init_app(app)
    # db.create_all()
    login_manager.init_app(app)
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')
    return app

def register_blueprint(app):
    from app.home import home as blueprint_home
    from app.admin import admin as blueprint_admin
    app.register_blueprint(blueprint_home)
    app.register_blueprint(blueprint_admin,url_prefix='/admin')

from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
#实例化App
ins=create_app()