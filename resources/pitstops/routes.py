from flask import request

from flask.views import MethodView


from . import bp
from schemas import PitstopsSchema
from db import pitstops



@bp.route('/pitstops')
class PitstopsList(MethodView):

    @bp.arguments(PitstopsSchema)
    def post(self, data):
        data = request.get_json()
        pitstops[data['position']] = data
        return{'Pitstop has been created successfully!' : pitstops[data['position']]}, 201

    @bp.response(200, PitstopsSchema(many=True))
    def get(self):
        try:
            return list(pitstops.values())
        except:
            return {'message':"Failed to get pitstops"}, 400

@bp.route('/pitstops/<int:position>')
class Pitstops(MethodView):

    @bp.response(200, PitstopsSchema)
    def get(self, position):
        if position in pitstops:
            return pitstops[position]
        return {'message' : "invalid pitstop"}, 400

    @bp.arguments(PitstopsSchema)
    def put(self, data, position):
        if position in pitstops:
            pitstops[position] = {k:v for k,v in data.items()}
            return {'message' : f'Pitstop {position} updated successfully.'}
        return {'error' : 'Position out of range(1-10)'}



    def delete(self,position):
        if position in pitstops:
            del pitstops[position]
            return {'message' : 'The pitstop has been deleted'}
        return {'error' : 'Pitstop does not exist in the Database.'}, 400