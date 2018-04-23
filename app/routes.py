# routes

from config import app
from flask import render_template, jsonify
import threading
from time import time, sleep
from random import randint

_lastTime = 0
_alive = False
_data = 0
_semiLock = threading.Semaphore()
_running = 0



@app.before_request
def before_request():
    # close the existing thread on background everytime that route configuration changed
    global _alive, _lastTime, _data, _semiLock
    if _alive:
        with _semiLock:
            _alive = False


def handler():
    # handle somthing synchrounus, this is an example non blocking operation in sync mode
    global _data, _alive, _lastTime, _semiLock
    print '>> thread'
    while _alive:
        if time() - _lastTime > 3:
            with _semiLock:
                _data = 1 + _data
                _alive = False

        sleep(0.3) # delay must be lower than the value from origin thread kill
    print '<< thread'



@app.route('/activate', methods=['POST'])
def activate():
    global _alive, _lastTime, _data, _semiLock, _running

    _running = _running + 1


    tmp = randint(10000, 99999)
    print('/activate --> thread ' + str(tmp) + ' started --> ' + str(_running))

    # origin thread kill
    # check if thread is alive, kill it
    if _alive:
        # do it with semaphore to keep objects aligned
        with _semiLock:
            _alive = False
        # wait for thread to get killed.
        sleep(0.5)

    # change state of thread to alive
    with _semiLock:
        _alive = True


    # run a thread
    _lastTime = time()
    trd = threading.Thread(target=handler)
    trd.start()
    # and join it current context to make interpreter stay on this current line
    trd.join()


    _running = _running - 1

    print('/activate <-- thread ' + str(tmp) + ' stopped <-- ' + str(_running))
    return jsonify({'name': 'hello', 'data': _data})


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/settings')
def settings():
    return render_template('settings.html')
