import os
import sys
# import sqlite3
from flask import Flask, jsonify, render_template

# Stop writing Object Code
sys.dont_write_bytecode = True

# Project Specific modules
# from models import Model

# Init app
app = Flask(__name__)
# db = Model("result_info.db")

@app.route('/')
def root():
    # return str(db.fetch())
    # return render_template('index.html')
    return "Hello World"

# @app.route("/<roll>")
# def search(roll):
#     return jsonify({"messages": [dict(row) for row in db.fetch(roll)]})

# Run app
if __name__ == "__main__":
    app.port = int(os.getenv('PORT', 5000))
    app.run(debug=True)


# db.done()
