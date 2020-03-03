import sys
from flask import Flask

# Stop writing Object Code
sys.dont_write_bytecode = True

# Route
from route import *

# app Instance
app = Flask(__name__)

if __name__ == "__main__":
    # Debugging Enabled
    app.debug = True
    # Get the port number from environment
    app.port = int(os.environ.get("PORT", 5000))
    # Run the app
    app.run()
    # Close Database
    db.done()
