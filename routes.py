from app import app, db
from flask import Blueprint, jsonify, render_template

@app.route('/')
def root():
    # return str(db.fetch())
    return render_template('index.html')

@app.route("/<roll>")
def search(roll):
    return jsonify({"messages": [ dict(row) for row in db.fetch(roll) ]})
