import os
import sys
from flask import Flask

# Stop writing Object Code
sys.dont_write_bytecode = True

# Project Specific modules
import views
from views import db

# app Initialization
app = Flask(__name__)

# Routes
app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/result/', view_func=views.result_fallback)
app.add_url_rule('/result/<roll>', view_func=views.result)

if __name__ == "__main__":
    # Debugging Enabled
    app.debug = True
    # Get the port number from environment
    app.port = int(os.environ.get("PORT", 5000))
    # Run the app
    app.run()
    # Close Database
    db.done()
