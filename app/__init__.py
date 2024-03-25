from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)


f1db = SQLAlchemy(app)
migrate = Migrate(app, f1db)

from models.fl_model import FL_Model
from models.ps_model import PS_Model

from resources.fastest_lap import bp as fl_bp
app.register_blueprint(fl_bp)

from resources.pitstops import bp as ps_bp
app.register_blueprint(ps_bp)

