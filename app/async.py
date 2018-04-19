from app import app

from flask_socketio import join_room, send, emit


@app.socket.on('connect')
def connect():
    app.publish('hello', 'you')


@app.socket.on('update')
def update():
    app.aio.worker()

