from flask import request
from flask.views import MethodView
from flask_smorest import abort
from . import bp
from schemas import Fastest_lapSchema
# from db import fastest_laps

from models.fl_model import FL_Model

@bp.route('/fastestlaps')
class FastestlapsList(MethodView):
    @bp.arguments(Fastest_lapSchema)
    def post(self, data):
        try:

            fl = FL_Model()
            fl.from_dict(data)
            fl.save_fl()
            return{'Fastest lap has been created successfully!' : f" Round {fl.round}'s fastest lap has been created."}, 201
        
        except:
            return{
                'error' : 'Unable to create fastest lap'
            }, 400
        

    @bp.response(200, Fastest_lapSchema(many=True))
    def get(self):
        try:
            return FL_Model.query.all()
        except:
            return {'message':"Failed to get fastest laps"}, 400
        
@bp.route('/fastestlaps/<int:id>')
class Fastestlaps(MethodView):

    @bp.response(200, Fastest_lapSchema)
    def get(self, id):
        fl = FL_Model.query.get(id)
        if fl:
            return fl
        
        else:
            abort(400, message = 'not a valid fastest lap')
        

    @bp.arguments(Fastest_lapSchema)
    def put(self, data, id):
        fl = FL_Model.query.get(id)
        if fl:
            fl.from_dict(data)
            fl.save_fl()
            return {"message" : "fastest lap updated successfully"}, 200
        else:
            abort(400, message = 'not a valid fastest lap')
       


    def delete(self, id):
        fl = FL_Model.query.get(id)
        if fl:
            fl.del_fl()
            return {"message" : "fastest lap has been deleted"},200
        else:
            abort(400, message = 'not a valid fastest lap')
  