"""

Before running install mysql connector for the required operating
system platform. Then install python-intercom using pip command

"""

import mysql.connector
from intercom.client import Client

# Connect to the intercom API using the personal access token
intercom = Client(personal_access_token='my_personal_access_token')

# Connect to the database. I am using localhost for testing
db = mysql.connector.connect(host="localhost",
                     user="root",
                     passwd="",
                     database="user")
executer = db.cursor()

# Execute the querry
executer.execute("SELECT * FROM USER")

# Fetch all the rows and use them to make user on intercom
for ids, name, email in executer.fetchall():
    user = intercom.users.create(id=ids, email=email, name=name)
    
db.close()