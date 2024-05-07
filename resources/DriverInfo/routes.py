from flask import request

from flask.views import MethodView
from flask_smorest import abort

from . import bp
from schemas import DriverInfoSchema


from models.di_model import Di_Model



@bp.route('/driverinfo')
class DriverInfoList(MethodView):
    
    @bp.arguments(DriverInfoSchema)
    def post(self, data):
        
        try:
            di = Di_Model()
            di.from_dict(data)
            di.save_di()
            return{'Driver info has been created successfully!' : f"{di.driver}'s info has been created"}, 201

        except:
            return{
                'error' : 'Unable to create Driver info'
            }, 400
        

    @bp.response(200, DriverInfoSchema(many=True))
    def get(self):
        try:
            return Di_Model.query.all()
        except:
            return {'message':"Failed to get driver info"}, 400

@bp.route('/driverinfo/<int:id>')
class DriverInfo(MethodView):

    @bp.response(200, DriverInfoSchema)
    def get(self, id):
        di = Di_Model.query.get(id)
        if di:
            return di

        else:
            abort(400, message = 'not a valid request')
  
    
    @bp.arguments(DriverInfoSchema)
    def put(self, data, id):
        di = Di_Model.query.get(id)
        if di:
            di.from_dict(data)
            di.save_di()
            return {"message" : "Driver info updated successfully"}, 200
        else:
            abort(400, message = 'not a valid request')



   
    def delete(self,id):
        di = Di_Model.query.get(id)
        if di:
            di.del_di()
            return {"message" : "Driver info has been deleted"},200
        else:
            abort(400, message = 'not a valid request')

