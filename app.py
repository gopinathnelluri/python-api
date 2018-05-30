#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import reqparse, Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///vehicle.db')
app = Flask(__name__)
api = Api(app)



class Vehicles(Resource):
    def get(self):
        conn = db_connect.connect()
        result = conn.execute("select * from vehicle_data") # This line performs query and returns json result
        #conn.close()
        data = result.cursor.fetchall()
        vehicles = []

        for row in data:
            temp = {
                "vehicle_id": row[0],
                "brand" : row[3],
                "model" : row[1],
                "year" : row[2],
                "speed": row[4],
                "type" : row[5],
                "description": row[6] 
            }
            vehicles.append(temp)
        return {'vehicles': vehicles} #[i[0] for i in query.cursor.fetchall()] # Fetches first column that is Employee ID
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('model')
        parser.add_argument('year')
        parser.add_argument('brand')
        parser.add_argument('speed')
        parser.add_argument('type')
        parser.add_argument('description')
        args = parser.parse_args()
        conn = db_connect.connect()
        """  
        query = conn.execute("insert into vehicle_data values(null,'{0}',{1},'{2}','{3}', \
                             '{4}','{5}')".format(args['model'],args['year'],args['brand'],
                             args['speed'], args['type'], args['description']))
        """  

        query = "insert into vehicle_data values(null,:model,:year,:brand,:speed,:type,:description)"
        result = conn.execute(query, model=args['model'],year=args['year'], \
                                     brand=args['brand'],speed=args['speed'], \
                                     type=args['type'], description=args['description'])
        return {"status":"success"}
  
   
api.add_resource(Vehicles, '/vehicles') # Route_1

if __name__ == '__main__':
     app.run()
