from __main__ import app, db
from flask import jsonify

@app.route('/')
def root():
    # return str(db.fetch())
    return "<center><h1>Hola Amigo!</h1></center>"

@app.route("/<roll>")
def search(roll):
    return jsonify([ dict(row) for row in db.fetch(roll) ])