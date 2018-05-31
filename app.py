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
        result = conn.execute("select * from vehicle_data")
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
        return vehicles
    
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
        query = "insert into vehicle_data values(null,:model,:year,:brand,:speed,:type,:description)"
        result = conn.execute(query, model=args['model'],year=args['year'], \
                                     brand=args['brand'],speed=args['speed'], \
                                     type=args['type'], description=args['description'])
        return {"status":"success"}

    def delete(self):
        conn = db_connect.connect()
        result = conn.execute("DELETE from vehicle_data order by v_id desc limit 1")
        return {"status":"success"}


class VehicleItem(Resource):
    def get(self,vehicle_id):
        conn = db_connect.connect()
        result = conn.execute("select * from vehicle_data where v_id = :v_id", v_id=vehicle_id) 
        data = result.cursor.fetchall()
        responseObject = {}
        for row in data:
            responseObject = {
                "vehicle_id": row[0],
                "brand" : row[3],
                "model" : row[1],
                "year" : row[2],
                "speed": row[4],
                "type" : row[5],
                "description": row[6] 
            }
            
        return responseObject
    
    def put(self,vehicle_id):
        parser = reqparse.RequestParser()
        parser.add_argument('model')
        parser.add_argument('year')
        parser.add_argument('brand')
        parser.add_argument('speed')
        parser.add_argument('type')
        parser.add_argument('description')
        args = parser.parse_args()
        conn = db_connect.connect()
        query = "UPDATE vehicle_data SET model = :model, year = :year, brand = :brand, speed = :speed, type = :type, description = :description where v_id = :v_id"
        result = conn.execute(query, model=args['model'],year=args['year'], \
                                     brand=args['brand'],speed=args['speed'], \
                                     type=args['type'], description=args['description'], v_id=vehicle_id)
        return {"status":"success"}
    
    def delete(self,vehicle_id):
        conn = db_connect.connect()
        result = conn.execute("DELETE from vehicle_data where v_id = :v_id", v_id=vehicle_id)
        return {"status":"success"}

class SearchTag(Resource):
    def get(self,tag1,tag2):
        conn = db_connect.connect()
        query = ""
        finaltag = ""
        if tag1=="model":
            query = "select * from vehicle_data where model like :tag"
            finaltag = "%"+tag2+"%"
        elif tag1=="year":
            query = "select * from vehicle_data where year = :tag"
            finaltag = tag2
        elif tag1=="brand":
            query = "select * from vehicle_data where brand like :tag"
            finaltag = "%"+tag2+"%"
        elif tag1=="speed":
            query = "select * from vehicle_data where speed like :tag"
            finaltag = "%"+tag2+"%"
        elif tag1=="type":
            query = "select * from vehicle_data where type like :tag"
            finaltag = "%"+tag2+"%"
        elif tag1=="description":    
            query = "select * from vehicle_data where description like :tag"
            finaltag = "%"+tag2+"%"
        
        result = conn.execute(query, tag=finaltag) 
        data = result.cursor.fetchall()
        vehicles = []
        responseObject = {}
        for row in data:
            responseObject = {
                "vehicle_id": row[0],
                "brand" : row[3],
                "model" : row[1],
                "year" : row[2],
                "speed": row[4],
                "type" : row[5],
                "description": row[6] 
            }
            vehicles.append(responseObject)
            
        return vehicles
   
api.add_resource(Vehicles, '/vehicles') # Route_1
api.add_resource(VehicleItem, '/vehicles/<string:vehicle_id>') # Route_2
api.add_resource(SearchTag, '/vehicles/search/<string:tag1>/<string:tag2>') # Route_3

if __name__ == '__main__':
     app.run()
