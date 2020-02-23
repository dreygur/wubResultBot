from app import db
from flask import Blueprint, jsonify, render_template

route = Blueprint('routes', __name__, template_folder='templates')

@app.route('/')
def root():
    # return str(db.fetch())
    return render_template('index.html')

@app.route("/<roll>")
def search(roll):
    return jsonify({"messages": [ dict(row) for row in db.fetch(roll) ]})
