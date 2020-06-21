from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "dkshkldjflsd"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///rcffutminna.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def create_db():
    db.create_all()
    print("Database Created Successfully")

from main_app import routes


@app.before_first_request
def create_db_command():
    create_db()