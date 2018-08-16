from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

from app import Resource
from flask_bootstrap import Bootstrap
Bootstrap(app)