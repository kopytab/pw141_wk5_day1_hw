from flask import request

from flask.views import MethodView
from flask_smorest import abort

from . import bp
from schemas import ConstructorInfoSchema


from models.ci_model import Ci_Model



@bp.route('/constructorinfo')
class ConstructorInfoList(MethodView):
    
    @bp.arguments(ConstructorInfoSchema)
    def post(self, data):
        
        try:
            ci = Ci_Model()
            ci.from_dict(data)
            ci.save_ci()
            return{'constructor info has been created successfully!' : f"{ci.fullname}'s info has been created"}, 201

        except:
            return{
                'error' : 'Unable to create constructor info'
            }, 400
        

    @bp.response(200, ConstructorInfoSchema(many=True))
    def get(self):
        try:
            return Ci_Model.query.all()
        except:
            return {'message':"Failed to get constructor info"}, 400

@bp.route('/constructorinfo/<int:id>')
class ConstructorInfo(MethodView):

    @bp.response(200, ConstructorInfoSchema)
    def get(self, id):
        ci = Ci_Model.query.get(id)
        if ci:
            return ci

        else:
            abort(400, message = 'not a valid request')
  
    
    @bp.arguments(ConstructorInfoSchema)
    def put(self, data, id):
        ci = Ci_Model.query.get(id)
        if ci:
            ci.from_dict(data)
            ci.save_ci()
            return {"message" : "Driver info updated successfully"}, 200
        else:
            abort(400, message = 'not a valid request')



   
    def delete(self,id):
        ci = Ci_Model.query.get(id)
        if ci:
            ci.del_ci()
            return {"message" : "Driver info has been deleted"},200
        else:
            abort(400, message = 'not a valid request')
