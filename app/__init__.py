from flask import Flask
app = Flask(__name__)

def register_blueprints(app):
    from app.handlers.public import mod as public_module
    app.register_blueprint(public_module)

###############################################################################
# Main app setup
###############################################################################
def create_app():
    # Create Flask app
    app = Flask(__name__)

    # Register config for app
    with app.app_context():
        register_blueprints(app)

    return app


app = create_app()
