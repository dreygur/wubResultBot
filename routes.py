#!/use/bin/env python3

"""
    # Views file for WUB Result bot
    # Provides Database Acess to main app
    # Copyright@ Rakibul Yeasin <ryeasin03@gmail.com> <@dreygur>
"""

import os
import json
from flask import Flask, jsonify, render_template

# Project Specific modules
from models import Model
db = Model("result_info.db")
app = Flask(__name__)

@app.route('/')
def root():
    # return str(db.fetch())
    return render_template('index.html')

@app.route("/<roll>")
def search(roll):
    result = json.dumps([dict(row) for row in db.fetch(roll)][0])
    result = result[11:-2].replace('"', '')
    result = result.replace(', ', "\n")
    result = result.upper()
    return jsonify({"messages": [{"text": result}]})
