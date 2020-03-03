#!/usr/bin/env python3

"""
Routes loaction

Copyright@ Rakibul Yeasin <ryeasin03@gmail.com> <@dreygur>
"""
import os
import sys
from flask import jsonify, render_template

# Project Specific modules
from models import Model

# Init app
db = Model("result_info.db")

def index():
    # return str(db.fetch())
    return render_template('index.html')

def result_fallback():
    return "You reached out a wrong place."

def result(roll):
    result = db.fetch(roll)
    result = result.upper()
    return jsonify({"messages": [{"text": result}]})
