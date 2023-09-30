from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

app.config["SECRET_KEY"] = "LSYTH37654323QFSA5T535DFQW3gt67we52q3hjm.jop;ui7"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///image.db"
db = SQLAlchemy(app)

import src.routes