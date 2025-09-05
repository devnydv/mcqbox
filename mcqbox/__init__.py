from flask import Flask
from mcqbox.model import db



app = Flask(__name__)

app.secret_key ="doNotTryToSuck"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()


from mcqbox import route