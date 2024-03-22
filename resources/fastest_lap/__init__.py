from flask_smorest import Blueprint

bp = Blueprint("fastest_laps", __name__, description="routes for fastest_lap")

from . import routes