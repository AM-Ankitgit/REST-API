import mysql.connector
from configs.config import dbconfig,RESPONSE_HEADER
import sys
import json
from flask import request,make_response

""""
make_response() gives you a convenience interface, 
one that will take arguments in more formats than the flask.Response() object takes
"""

class user_model():
    # create the connection in constructor so whenever we need the connection of the mysql we can access
    def __init__(self): 
        host1=dbconfig['host']
        user1=dbconfig['user'] 
        password1=dbconfig['password']
        self.database1=dbconfig['database']

        #connection establishment 
        self.con = mysql.connector.connect(host=host1,user=user1,password=password1,database=self.database1)
        self.con.autocommit=True
        self.cur = self.con.cursor(dictionary=True) # cursor is agent
        
    def user_getall_model(self):

        self.cur.execute("SELECT * FROM user")
        data = self.cur.fetchall()
        if len(data)>0:
            res= make_response({'payload':data},200) #200 for ok, header response will create application-type:application/json
            res.headers['Access-Control-Allow-Origin']="*" # * allow all type request
            return res
        else:
            return make_response({'payload':"No data Found in database"},204) #204 for no-content
            # because of 204 will not send the payload no content mean no content
        
        
    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO USER(id,name,email,phone,role,password) \
                         VALUES('{data['id']}','{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        
        if self.cur.rowcount>0:
            return make_response({'payload':"Successfully Sumbited"},201)
        else:
            return make_response({'message':"already existed"},409)
    
    

    def user_update_model(self,data):
        self.cur.execute(f"UPDATE user SET id='{data['id']}',name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' \
                          WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return make_response({'payload':"Detail Updated"},201)
        else:
            return make_response({'payload':"Detail Not Updated"},202) #reauest cannot to be process 


    def user_delete_model(self,id):
        self.cur.execute(f"DELETE FROM user WHERE id={id}")
        
        return make_response({'payload': "Detail has been deleted" },200)
    
    def user_patch_model(self,data,id):
        q  = f"UPDATE user SET "
        for key in data:
            q+=f"{key}='{data[key]}',"
        q = q[:-1]+f" WHERE id={id}"

        self.cur.execute(q)

        if self.cur.rowcount>0:
            return make_response({'message': 'Detail Updated Successfully'},201)
        else:
            return make_response({'messgae':'Detail not Updated'},202)