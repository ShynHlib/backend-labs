from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)

db = SQLAlchemy(app)

import module.views
import module.models
