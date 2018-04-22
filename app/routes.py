from config import app
from flask import render_template, jsonify
import threading
from time import time, sleep
from random import randint

_lastTime = 0
_alive = False
_data = 0
_semiLock = threading.Semaphore()


@app.before_request
def before_request():
    global _alive, _lastTime, _data, _semiLock
    if _alive:
        with _semiLock:
            _alive = False
        sleep(0.2)


def handler():
    global _data, _alive, _lastTime, _semiLock

    while _alive:
        if time() - _lastTime > 10:
            with _semiLock:
                _data = 19 + _data
                _alive = False


@app.route('/activate', methods=['POST'])
def activate():
    global _alive, _lastTime, _data, _semiLock
    tmp = randint(1000, 9999)
    print(str(tmp) + ' activated')

    if _alive:
        with _semiLock:
            _alive = False
        sleep(0.5)

    with _semiLock:
        _alive = True

    _lastTime = time()
    trd = threading.Thread(target=handler)
    trd.start()
    trd.join()

    print(str(tmp) + ' deativated')
    return jsonify({'name': 'hello', 'data': _data})


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/settings')
def settings():
    return render_template('settings.html')
