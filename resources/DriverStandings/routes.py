from flask import request

from flask.views import MethodView
from flask_smorest import abort

from . import bp
from schemas import DriverStandingsSchema


from models.ds_model import Ds_Model



@bp.route('/driverstandings')
class DriverStandingsList(MethodView):
    
    @bp.arguments(DriverStandingsSchema)
    def post(self, data):
        
        try:
            DsEntry = Ds_Model()
            DsEntry.from_dict(data)
            DsEntry.save_ds()
            return{'Entry has been created successfully!' : f"{DsEntry.driver}'s entry has been created"}, 201

        except:
            return{
                'error' : 'Unable to create entry'
            }, 400
        

    @bp.response(200, DriverStandingsSchema(many=True))
    def get(self):
        try:
            return Ds_Model.query.all()
        except:
            return {'message':"Failed to get driver standings"}, 400

@bp.route('/driverstandings/<int:id>')
class DriverStandingsEntry(MethodView):

    @bp.response(200, DriverStandingsSchema)
    def get(self, id):
        entry = Ds_Model.query.get(id)
        if entry:
            return entry

        else:
            abort(400, message = 'not a valid entry')
  
    
    @bp.arguments(DriverStandingsSchema)
    def put(self, data, id):
        entry = Ds_Model.query.get(id)
        if entry:
            entry.from_dict(data)
            entry.save_ds()
            return {"message" : "entry updated successfully"}, 200
        else:
            abort(400, message = 'not a valid entry')



   
    def delete(self,id):
        entry = Ds_Model.query.get(id)
        if entry:
            entry.del_ds()
            return {"message" : "entry has been deleted"},200
        else:
            abort(400, message = 'not a valid entry')

