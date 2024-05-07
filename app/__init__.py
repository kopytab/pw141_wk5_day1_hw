import json
from flask import Flask, request, jsonify
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager

from Config import Config
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
jwt = JWTManager(app)
CORS(app)


f1db = SQLAlchemy(app)
migrate = Migrate(app, f1db)

from models.fl_model import FL_Model
from models.ps_model import PS_Model
from models.ci_model import Ci_Model
from models.cs_model import Cs_Model
from models.di_model import Di_Model
from models.ds_model import Ds_Model
from models.sched_model import Sched_Model

from resources.fastest_lap import bp as fl_bp
app.register_blueprint(fl_bp)

from resources.pitstops import bp as ps_bp
app.register_blueprint(ps_bp)

from resources.ConstructorInfo import bp as ci_bp
app.register_blueprint(ci_bp)

from resources.ConstructorStandings import bp as cs_bp
app.register_blueprint(cs_bp)

from resources.DriverInfo import bp as di_bp
app.register_blueprint(di_bp)

from resources.DriverStandings import bp as ds_bp
app.register_blueprint(ds_bp)

from resources.Schedule import bp as sched_bp
app.register_blueprint(sched_bp)