from model.user_models import user_model
from configs.config import upload_folder
from flask import Blueprint,request,send_file
import os
from datetime import datetime


user_control = Blueprint('user',__name__)

"""
In every route keep the same prefix 
After deploymet on server the nginx will loop for the prefix of the route
we will set new as the starting of the all route 

"""
obj   = user_model()
@user_control.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()


#post method to add the data
@user_control.route("/user/addone",methods=['POST'])
def user_addone_controller():
    data = request.form
    return obj.user_addone_model(data)


#it work similar to the post but it quit differnt here we update the existing record
@user_control.route("/user/update",methods=['PUT'])
def user_update_controller():
    data = request.form
    return obj.user_update_model(data)


# to delete the perticular record base on id
@user_control.route("/user/delete/<id>",methods=['DELETE'])
def user_delete_controller(id):
    return obj.user_delete_model(id)

# in above put we need pass the whole record to update the record 
# in patch only we can pass what all thing need to be updated
@user_control.route("/user/patch/<id>",methods=['PATCH'])
def user_patch_controller(id):
    data = request.form
    return obj.user_patch_model(data,id)



#pagination  
@user_control.route("/user/getall/limit/<limit>/page/<page>", methods=['GET'])
def user_pagination_controller(limit,page):
    return obj.user_pagination_model(limit,page)

#upload file(POSTMAN) to the server
#saving file into filesytem with unique filenama
# updating filepath in database with respective entity

# here we will use put method to full fill above three condition
# put : to update 
# USE POSTMAN


@user_control.route("/user/<uid>/upload/avatar",methods=['PUT']) # uid refer to unique id for perticular avatar
def user_avatar_controller(uid):
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    
    #create unique file name for each uid
    unique_file = str(datetime.now().timestamp()).replace(".","")
    file  = request.files['AM']
    ext   = (os.path.basename(file.filename).split("."))[-1]
    avatar_name = f"{unique_file}.{ext}"
    file_name= os.path.join(upload_folder,avatar_name)
    
    #save the file upload folder
    file.save(file_name)
    # to get the of avatar , need to store the name of avatar in db first
    return   obj.user_avatar_model(uid,avatar_name)


@user_control.route("/user/upload/<filename>")
def user_get_avatar(filename):
    avatar_path = os.path.join(upload_folder,filename)
    return send_file(avatar_path)
    
@user_control.route("/user/get_upload_data",methods=['GET'])
def get_upload_data():
    # with open('data.txt','r') as f:
    #     text = f.readlines()
    return  send_file('data.txt')