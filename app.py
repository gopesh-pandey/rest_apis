from flask import Flask, jsonify
from flask import Flask, request
from flask_restful import Resource, Api
#from sqlalchemy import create_engine
from json import dumps
import MySQLdb


#Create a engine for connecting to SQLite3.
#Assuming salaries.db is in your app root folder

#e = create_engine('sqlite:///salaries.db')
# Connect
db = MySQLdb.connect(host="letstestdb.mysql.database.azure.com",user="myadmin@letstestdb",passwd="Welcome12@admin",db="mysampledb")

app = Flask(__name__)
api = Api(app)

class Departments_Meta(Resource):
        def get(self):
                #Connect to databse

                cursor = db.cursor()
                #Perform query and return JSON data
                cursor.execute("select distinct product_name from products")
                r = [dict((cursor.description[i][0], value)
                        for i, value in enumerate(row)) for row in cursor.fetchall()]
                return jsonify({'myCollection' : r})
                #return {'departments': [i[0] for i in query.cursor.fetchall()]}

class Departmental_Salary(Resource):
    def get(self, department_name):
        #conn = e.connect()
        cursor = db.cursor()
        cursor.execute("select * from products where geography='%s'"%department_name.upper())

        r = [dict((cursor.description[i][0], value)
                        for i, value in enumerate(row)) for row in cursor.fetchall()]
        return jsonify({'myCollection' : r})
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        #result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        #return result
    #We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient

api.add_resource(Departmental_Salary, '/dept/<string:department_name>')
api.add_resource(Departments_Meta, '/departments')

if __name__ == '__main__':
    app.run(debug=True)
