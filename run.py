#!/usr/bin/env python

from app.app import app
from threading import Thread, Event
import time
import os


def subscribe_handler(action, message):
    if action == 'hello':
        app.socket.emit('reply-to-someone', message, broadcast=True)
        time.sleep(0.2)
    pass


def service_handler(ev):
    print(' * Thread worker [ONLINE] ')
    while ev.is_set():
        time.sleep(2)


def flask_handler(ev):
    print(' * SocketIO and Flask [ONLINE] ')
    app.aio.attach(subscribe_handler)
    app.socket.run(app)


if __name__ == '__main__':
    event = Event()
    try:
        event.set()
        main_thread = Thread(target=service_handler, args=(event,))
        flask_thread = Thread(target=flask_handler, args=(event,))
        main_thread.start()
        time.sleep(0.2)
        flask_thread.start()

        while 1:
            time.sleep(0.5)
    except KeyboardInterrupt:
        print(' * Terminating... ')
        event.clear()
        os.system('kill -9 %d' % os.getpid())
