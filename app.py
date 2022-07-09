from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
import json

file_path = os.path.abspath(os.getcwd())+"\\usernames.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://ufecgkfjiqzgfa:ade59c25b70cd74b8bf574ae4958bb0b2ba649399333e8d9b42f864036c63129@ec2-44-195-162-77.compute-1.amazonaws.com:5432/d1ncuitteasauf'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    listOfInts = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route("/<user>/<password>/<listInts>")
def hello_worsda(user, password, listInts):
    user = User(username=user, email=password,
                listOfInts=json.dumps(list(listInts)))
    db.session.add(user)
    db.session.commit()
    print(user)
    return "success"


@app.route("/login/<user>/<password>")
def hello_worasdld(user, password):
    if User.query.filter_by(username=user).first() != None and password == User.query.filter_by(username=user).first().email:
        user = User.query.filter_by(username=user).first()
        return jsonify(json.loads(user.listOfInts))
    return "failure"


if __name__ == "__main__":
    app.run(debug=True)
