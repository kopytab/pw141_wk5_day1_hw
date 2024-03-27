from flask import request

from flask.views import MethodView
from flask_smorest import abort
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager

from . import bp
from schemas import PitstopsSchema
# from db import pitstops

from models.ps_model import PS_Model



@bp.route('/pitstops')
class PitstopsList(MethodView):
    @jwt_required()
    @bp.arguments(PitstopsSchema)
    def post(self, data):
        
        try:
            ps = PS_Model()
            ps.from_dict(data)
            ps.save_ps()
            return{'Pitstop has been created successfully!' : f"{ps.driver}'s pit stop has been created"}, 201

        except:
            return{
                'error' : 'Unable to create pit stop'
            }, 400
        

    @bp.response(200, PitstopsSchema(many=True))
    def get(self):
        try:
            return PS_Model.query.all()
        except:
            return {'message':"Failed to get pitstops"}, 400

@bp.route('/pitstops/<int:id>')
class Pitstops(MethodView):

    @bp.response(200, PitstopsSchema)
    def get(self, id):
        ps = PS_Model.query.get(id)
        if ps:
            return ps

        else:
            abort(400, message = 'not a valid pit stop')
  
    @jwt_required()
    @bp.arguments(PitstopsSchema)
    def put(self, data, id):
        ps = PS_Model.query.get(id)
        if ps:
            ps.from_dict(data)
            ps.save_ps()
            return {"message" : "pit stop updated successfully"}, 200
        else:
            abort(400, message = 'not a valid pit stop')



    @jwt_required()
    def delete(self,id):
        ps = PS_Model.query.get(id)
        if ps:
            ps.del_ps()
            return {"message" : "pit stop has been deleted"},200
        else:
            abort(400, message = 'not a valid pit stop')

