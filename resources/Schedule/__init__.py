from flask_smorest import Blueprint

bp = Blueprint("schedule", __name__, description="routes for schedule")

from . import routes