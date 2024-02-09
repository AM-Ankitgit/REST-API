import os
if os.name=='nt':
    dbconfig = {'host':"localhost",'port':3306,'user':'root','password':os.getenv('MYSQL_PASSWORD'),'database':'jan_flask_api'}
else:
    dbconfig = {'host':"localhost",'port':3306,'user':'brain','password':"Brain@1927#",'database':'jan_flask_api'}

upload_folder = "artifacts"


RESPONSE_HEADER = {
    "Content-Type": "application/json",
    'Access-Control-Allow-origin':"*"
    }