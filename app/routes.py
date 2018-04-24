from config import app, publish, store, socket
from flask import render_template, request

from time import time
store['clients'] = []


@socket.on('connect')
def socket_connect():
    socket.emit('auth', request.sid);
    store['clients'].append(request.sid)


@socket.on('disconnect')
def socket_disconnect():
    store['clients'].remove(request.sid)


@socket.on('temp')
def temp(data):
    socket.emit('message', str(data), room=request.sid)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send')
def send():
    for d in store['clients']:
        publish('message', d)
    return "ok"
