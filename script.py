from flask import Flask
from flask import jsonify
import random as rnd
import os


app = Flask(__name__)

@app.route('/')
def root():
    return "Hello World"

@app.route('/api/<name>')
def api(name):
    welcome_text = [

        "Hi ",
        "Hello ",
        "Welcome "
        ]

    return jsonify({
        "messages": [
            {"text": rnd.choice(welcome_text) + str(name)},
        ]
})

if __name__=='__main__':
    app.debug = True
    app.port = int(os.environ.get('PORT', 5000))
    app.run()