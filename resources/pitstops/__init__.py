from flask_smorest import Blueprint

bp = Blueprint("pitstops", __name__, description="routes for pitstops")

from . import routes