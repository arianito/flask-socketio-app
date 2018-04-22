from config import app
from time import sleep


def handle(action, message):
    if action == 'hello':
        app.socket.emit('reply-to-someone', message, broadcast=True)
        sleep(0.2)

    if action == "finger":
        app.socket.emit('finger-detected', message, broadcast=True)
        sleep(2)
        pass
