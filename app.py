import os
import sys
import json
from flask import Flask, jsonify, render_template

# Stop writing Object Code
sys.dont_write_bytecode = True

# Project Specific modules
from routes import *

# Run app
if __name__ == "__main__":
    app.debug = True
    app.port = int(os.environ.get("PORT", 5000))
    app.run()
    db.done()
