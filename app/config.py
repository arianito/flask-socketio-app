from flask import Flask, send_file
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

import routes


@app.errorhandler(IOError)
def handle_invalid_usage(error):
    return 'error'


@app.route('/<path:path>')
def static_file(path):
    temp = os.path.dirname(os.path.realpath(__file__)) + '/public/' + path
    return send_file(temp)
