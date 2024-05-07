from flask_smorest import Blueprint

bp = Blueprint("driver_standings", __name__, description="routes for driver standings")

from . import routes