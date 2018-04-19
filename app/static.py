from app import app
from flask import render_template, send_file
import os


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/settings')
def settings():
    return render_template('settings.html')


op = 0


@app.route('/exit')
def exit():
    os.system('kill %d' % os.getpid())


@app.route('/send')
def send():
    global op
    op = op + 1
    app.publish("hello", "from send " + str(op))
    return "ok"


@app.route('/<path:path>')
def static_file(path):
    temp = os.path.dirname(os.path.realpath(__file__)) + '/public/' + path
    return send_file(temp)
