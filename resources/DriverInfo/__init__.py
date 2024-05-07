from flask_smorest import Blueprint

bp = Blueprint("driver_info", __name__, description="routes for driver info")

from . import routes