import os
dbconfig = {'host':"localhost",'port':3306,'user':'root','password':os.getenv('MYSQL_PASSWORD'),'database':'jan_flask_api'
}