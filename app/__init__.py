from flask import Flask

app = Flask(__name__)

from resources.pitstops import routes
from resources.fastest_lap import routes