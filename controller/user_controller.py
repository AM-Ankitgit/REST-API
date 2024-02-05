from model.user_models import user_model
from flask import Blueprint,request


user_control = Blueprint('user',__name__)


obj   = user_model()
@user_control.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()



@user_control.route("/user/addone",methods=['PUT'])
def user_addone_controller():
    data = request.form
    return obj.user_addone_model(data)




@user_control.route("/user/update",methods=['POST'])
def user_update_controller():
    data = request.form
    return obj.user_update_model(data)



@user_control.route("/user/delete/<id>",methods=['DELETE'])
def user_delete_controller(id):
    return obj.user_delete_model(id)