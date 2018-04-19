from config import app
from flask import render_template

op = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/settings')
def settings():
    return render_template('settings.html')


@app.route('/send')
def send():
    global op
    op = op + 1
    app.publish("hello", "from send " + str(op))
    return "ok"
