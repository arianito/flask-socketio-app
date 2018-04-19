from flask import Flask, send_file
from flask_socketio import SocketIO
from pubsub import PubSub
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.socket = SocketIO(app)
app.aio = PubSub()
app.publish = app.aio.publish

import routes
import socketio


@app.route('/<path:path>')
def static_file(path):
    temp = os.path.dirname(os.path.realpath(__file__)) + '/public/' + path
    return send_file(temp)
