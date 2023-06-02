from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/hari"
app.config["SECRET_KEY"] = "6adc7c138b37b201cae11ecdbac1a13da5e5f2ee"

#setup
mongodb_client = PyMongo(app)
db = mongodb_client.db


from application import routes