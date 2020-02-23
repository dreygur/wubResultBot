import os
import sys
import sqlite3
from flask import Flask, jsonify, render_template

# Stop writing Object Code
sys.dont_write_bytecode = True

# Project Specific modules
from models import Model

# Init app
app = Flask(__name__)
db = Model("result_info.db")
import routes

# Run app
if __name__ == "__main__":
    app.port = int(os.getenv('PORT', 5000))
    app.run(debug=True)
    db.done()