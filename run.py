#!/usr/bin/env python

from app.config import app
from app import subscribe
from app import realtime

from threading import Thread, Event
import time
import os


def service_handler(ev):
    print(' * Thread worker [ONLINE] ')
    while ev.is_set():
        realtime.run()


def flask_handler():
    print(' * SocketIO and Flask [ONLINE] ')
    app.aio.attach(subscribe.handle)
    app.socket.run(app)


if __name__ == '__main__':
    event = Event()
    try:
        event.set()
        main_thread = Thread(target=service_handler, args=(event,))
        flask_thread = Thread(target=flask_handler)
        flask_thread.start()
        time.sleep(0.5)
        main_thread.start()

        while 1:
            time.sleep(0.5)
    except KeyboardInterrupt:
        print(' * Terminating... ')
        event.clear()
        os.system('kill -9 %d' % os.getpid())
