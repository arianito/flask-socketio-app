from app.config import app

if __name__ == '__main__':
    app.run(threaded=True, debug=False, port=8000)
