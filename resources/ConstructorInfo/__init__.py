from flask_smorest import Blueprint

bp = Blueprint("constructor_info", __name__, description="routes for constructor info")

from . import routes