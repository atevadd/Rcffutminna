from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = "dkshkldjflsd"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///rcffutminna.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

def create_db():
    db.create_all() 
    print("Database Created Successfully") 

from main_app import routes
from main_app.models import User


@app.before_first_request
def create_db_command():
    create_db()
    find_user = User.query.filter_by(username="arinze").first()
    if not find_user:
        user = User(username="arinze",password="password")
        db.session.add(user)
        db.session.commit()
    else:
        print("User already exists!")
