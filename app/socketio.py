from config import app


@app.socket.on('connect')
def connect():
    app.publish('hello', 'you are connected.')


@app.socket.on('disconnect')
def connect():
    app.publish('hello', 'you are connected.')


@app.socket.on('update')
def update():
    app.aio.worker()
