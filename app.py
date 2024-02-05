# to create function for app
from flask import Flask
from controller.user_controller import user_control as us


# to create function fo
def create_app():
    app = Flask(__name__)
    app.register_blueprint(us)

    return app