from flask import Flask
from flask_socketio import SocketIO
from app.pubsub import PubSub

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

app.socket = SocketIO(app)
app.aio = PubSub()

app.publish = app.aio.publish

