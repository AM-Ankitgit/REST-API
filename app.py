# to create function for app
from flask import Flask
from controller.user_controller import user_control as us

# # to create function 
app = Flask(__name__)
app.register_blueprint(us)

if __name__ == "__main__":
    app.run(port=5002)











