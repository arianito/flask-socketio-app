from config import app
from flask import render_template, jsonify
from threading import Thread
from time import time, sleep

last_time = 0
alive = False


def handler():
    global alive, last_time
    while alive:
        if time() - last_time > 10:
            alive = False
            last_time = time()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/activate', methods=['POST'])
def activate():
    global alive
    if alive:
        alive = False

    sleep(0.3)
    trd = Thread(target=handler)
    trd.start()
    trd.join()
    return jsonify({'name': 'hello'})


@app.route('/settings')
def settings():
    return render_template('settings.html')
