import os
import sys
import json
from flask import Flask, jsonify, render_template

# Stop writing Object Code
sys.dont_write_bytecode = True

# Project Specific modules
from models import Model

# Init app
app = Flask(__name__)
db = Model("result_info.db")

@app.route('/')
def root():
    # return str(db.fetch())
    return render_template('index.html')

@app.route("/<roll>")
def search(roll):
    result = json.dumps([dict(row) for row in db.fetch(roll)][0])
    return jsonify({"messages": [{"text": result[11:-2]}]})

# Run app
if __name__ == "__main__":
    app.port = int(os.environ.get('PORT', 5000))
    app.run(debug=True)
    db.done()
