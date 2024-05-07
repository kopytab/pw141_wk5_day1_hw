from flask_smorest import Blueprint

bp = Blueprint("constructor_standings", __name__, description="routes for constructor standings")

from . import routes