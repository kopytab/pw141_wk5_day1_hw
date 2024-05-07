from flask import request

from flask.views import MethodView
from flask_smorest import abort

from . import bp
from schemas import ScheduleSchema


from models.sched_model import Sched_Model



@bp.route('/schedule')
class ScheduleList(MethodView):
    
    @bp.arguments(ScheduleSchema)
    def post(self, data):
        
        try:
            schedule = Sched_Model()
            schedule.from_dict(data)
            schedule.save_sched()
            return{'Scheduled race has been created successfully!' : f"{schedule.country}'s race has been created"}, 201

        except:
            return{
                'error' : 'Unable to create scheduled race'
            }, 400
        

    @bp.response(200, ScheduleSchema(many=True))
    def get(self):
        try:
            return Sched_Model.query.all()
        except:
            return {'message':"Failed to get schedule"}, 400

@bp.route('/schedule/<int:id>')
class Schedule(MethodView):

    @bp.response(200, ScheduleSchema)
    def get(self, id):
        race = Sched_Model.query.get(id)
        if race:
            return race

        else:
            abort(400, message = 'not a valid race')
  
    
    @bp.arguments(ScheduleSchema)
    def put(self, data, id):
        race = Sched_Model.query.get(id)
        if race:
            race.from_dict(data)
            race.save_sched()
            return {"message" : "race updated successfully"}, 200
        else:
            abort(400, message = 'not a valid race')



   
    def delete(self,id):
        race = Sched_Model.query.get(id)
        if race:
            race.del_sched()
            return {"message" : "race has been deleted"},200
        else:
            abort(400, message = 'not a valid race')

