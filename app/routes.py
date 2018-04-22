from config import app
from flask import render_template, jsonify
import threading
from time import time, sleep
from random import randint

_last_time = 0
_alive = False
_data = 0


@app.before_request
def before_request():
    global _alive, _last_time, _data
    if _alive:
        _alive = False


def handler():
    global _data, _alive, _last_time

    while _alive:
        if time() - _last_time > 10:
            _data = 19 + _data
            _alive = False


@app.route('/activate', methods=['POST'])
def activate():
    global _alive, _last_time, _data
    tmp = randint(1000, 9999)
    print(str(tmp) + ' activated')

    if _alive:
        _alive = False
        sleep(0.5)
    _alive = True
    _last_time = time()
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
