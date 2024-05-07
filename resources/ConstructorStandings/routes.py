from flask import request

from flask.views import MethodView
from flask_smorest import abort

from . import bp
from schemas import ConstructorStandingsSchema


from models.cs_model import Cs_Model



@bp.route('/constructorstandings')
class ConstructorStandingsList(MethodView):
    
    @bp.arguments(ConstructorStandingsSchema)
    def post(self, data):
        
        try:
            CsEntry = Cs_Model()
            CsEntry.from_dict(data)
            CsEntry.save_cs()
            return{'Entry has been created successfully!' : f"{CsEntry.team}'s entry has been created"}, 201

        except:
            return{
                'error' : 'Unable to create entry'
            }, 400
        

    @bp.response(200, ConstructorStandingsSchema(many=True))
    def get(self):
        try:
            return Cs_Model.query.all()
        except:
            return {'message':"Failed to get constructor standings"}, 400

@bp.route('/constructorstandings/<int:id>')
class ConstructorStandingsEntry(MethodView):

    @bp.response(200, ConstructorStandingsSchema)
    def get(self, id):
        entry = Cs_Model.query.get(id)
        if entry:
            return entry

        else:
            abort(400, message = 'not a valid entry')
  
    
    @bp.arguments(ConstructorStandingsSchema)
    def put(self, data, id):
        entry = Cs_Model.query.get(id)
        if entry:
            entry.from_dict(data)
            entry.save_cs()
            return {"message" : "entry updated successfully"}, 200
        else:
            abort(400, message = 'not a valid entry')



   
    def delete(self,id):
        entry = Cs_Model.query.get(id)
        if entry:
            entry.del_cs()
            return {"message" : "entry has been deleted"},200
        else:
            abort(400, message = 'not a valid entry')

