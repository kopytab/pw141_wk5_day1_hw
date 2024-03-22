from flask import request
from flask.views import MethodView
from . import bp
from schemas import Fastest_lapSchema
from db import fastest_laps

@bp.route('/fastestlaps')
class FastestlapsList(MethodView):
    @bp.arguments(Fastest_lapSchema)
    def post(self, data):
        data = request.get_json()
        print(data)
        fastest_laps[data['round']] = data
        return{'Fastest lap has been created successfully!' : fastest_laps[data['round']]}, 201

    @bp.response(200, Fastest_lapSchema(many=True))
    def get(self):
        try:
            return list(fastest_laps.values())
        except:
            return {'message':"Failed to get fastest laps"}, 400
        
@bp.route('/fastestlaps/<int:round>')
class Fastestlaps(MethodView):

    @bp.response(200, Fastest_lapSchema)
    def get(self, round):
        if round in fastest_laps:
            return fastest_laps[round]
        return {'message' : "invalid round"}, 400
    @bp.arguments(Fastest_lapSchema)
    def put(self, data, round):
        data = request.get_json()
        if round in fastest_laps:
            fastest_laps[round] = data
            return {'Fastest lap updated successfully.' : fastest_laps[round]}, 201
        return {'error' : 'Race does not exist in the Database.'}, 400


    def delete(self, round):
        if round in fastest_laps:
            del fastest_laps[round]
            return {'Success': "The fastest lap has been deleted"},200
        return {'error' : 'Race does not exist in the Database.'}, 400

# @app.delete('/post')
# def delete_fastest_lap():
#     lap_data = request.get_json()
#     lap_race = lap_data['race']

#     if lap_race not in fastest_laps:
#         return { 'message' : "Invalid Post"}, 400
    
#     fastest_laps.pop(lap_race)
#     return {'The fastest lap has been deleted': f"{lap_race}'s fastest lap is no more. . . "}