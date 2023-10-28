from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
from flask_migrate import Migrate

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)

migrate = Migrate(app, db)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # dictionary = {}
        # for column in self.__table__.columns:
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        dictionary = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    cafes = Cafe.query.all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


## HTTP GET - Read Record
@app.route("/all")
def get_all():
    cafes = Cafe.query.all()
    return jsonify(cafe=[cafe.to_dict() for cafe in cafes])

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
