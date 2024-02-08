from model.user_models import user_model
from flask import Blueprint,request


user_control = Blueprint('user',__name__)

"""
In every route keep the same prefix 
After deploymet on server the nginx will loop for the prefix of the route
we will set new as the starting of the all route 

"""
obj   = user_model()
@user_control.route("/new/user/getall")
def user_getall_controller():
    return obj.user_getall_model()



@user_control.route("/new/user/addone",methods=['POST'])
def user_addone_controller():
    data = request.form
    return obj.user_addone_model(data)



@user_control.route("/new/user/update",methods=['PUT'])
def user_update_controller():
    data = request.form
    return obj.user_update_model(data)



@user_control.route("/new/user/delete/<id>",methods=['DELETE'])
def user_delete_controller(id):
    return obj.user_delete_model(id)


@user_control.route("/new/user/patch/<id>",methods=['PATCH'])
def user_patch_controller(id):
    data = request.form
    return obj.user_patch_model(data,id)
