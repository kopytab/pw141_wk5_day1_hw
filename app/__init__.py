from flask import Flask
from flask_smorest import Api

from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

from resources.fastest_lap import bp as fl_bp
app.register_blueprint(fl_bp)

from resources.pitstops import bp as ps_bp
app.register_blueprint(ps_bp)

