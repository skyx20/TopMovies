from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)
db = SQLAlchemy(app)


from app import routes, models
