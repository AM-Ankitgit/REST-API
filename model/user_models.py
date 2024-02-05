import mysql.connector
from configs.config import dbconfig
import sys
import json
from flask import request


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
            return {'payload':data}  # header response will create application-type:application/json
        else:
            return {'payload':"No data Found in database"} 
        # query = (f"SELECT name,email,role,password FROM {self.database1}")
        
        
    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO USER(id,name,email,phone,role,password) \
                         VALUES('{data['id']}','{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        
        return {'payload':"Successful"}
    
    

    def user_update_model(self,data):
        self.cur.execute(f"UPDATE user SET id='{data['id']}',name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' \
                          WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return {'payload':"Detail Updated"}
        else:
            return {'payload':"Detail Not Updated"}


    def user_delete_model(self,id):
        self.cur.execute(f"DELETE FROM user WHERE id={id}")
        
        return {'payload': "Detail has been deleted" }

