#!/usr/bin/env python3

"""
Routes loaction

Copyright@ Rakibul Yeasin <ryeasin03@gmail.com> <@dreygur>
"""
import os
import sys
import json
from flask import Flask, jsonify, render_template

# Project Specific modules
from models import Model

# Init app
app = Flask(__name__)
db = Model("result_info.db")

@app.route('/')
def root():
    # return str(db.fetch())
    return render_template('index.html')

@app.route("/result")
def result_fallback():
    return "You reached out a wrong place."

@app.route("/result/<roll>")
def result(roll):
    result = json.dumps([dict(row) for row in db.fetch(roll)][0])
    result = result[11:-2].replace('"', '')
    result = result.replace(', ', "\n")
    result = result.upper()
    return jsonify({"messages": [{"text": result}]})
