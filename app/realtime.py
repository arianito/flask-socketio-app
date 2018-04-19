from config import app
from time import sleep, time


def run():
    app.publish('hello', time())
    sleep(2.0)
