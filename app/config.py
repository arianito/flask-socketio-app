from flask import Flask, send_file
import os

# initializing flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'some secret key'

import routes

# serve static file and folders inside public directory
@app.route('/<path:path>')
def static_file(path):
    temp = os.path.dirname(os.path.realpath(__file__)) + '/public/' + path
    return send_file(temp)
