# Base file for initiating flask app
import os
from dotenv import load_dotenv

from flask import Flask
from flask_login import LoginManager
from app.config import VARS, ENV_VARS
from app.models import db

app = Flask(__name__)

###############################################################################
# Config
###############################################################################
def register_app_config(app):
    # On server will read from env variables
    load_dotenv()

    for k, v in VARS.items():
        app.config[k] = v
    for var in ENV_VARS:
        if os.environ.get(var):
            app.config[var] = os.environ.get(var)
    app.secret_key = app.config.get('SECRET_KEY')
    db.init_app(app)


def register_blueprints(app):
    # Not working because app.register_blueprints called before mod defined?
    # https://stackoverflow.com/questions/37954472/register-blueprint-doesnt-add-route-to-flask-app
    from app.handlers.public import mod as public_module
    app.register_blueprint(public_module)


def register_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    from app.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        """Loads active User object for LoginManager."""
        print('load user')
        return User.objects.get(id=user_id)
        # try:
        #     return User.objects.get(id=user_id)
        # except (DoesNotExist, ValidationError):
        #     return None

###############################################################################
# Main app setup
###############################################################################
def create_app():
    # Create Flask app
    app = Flask(__name__)

    # Configure app
    with app.app_context():
        register_app_config(app)
        register_blueprints(app)
        register_login(app)

    return app


app = create_app()
