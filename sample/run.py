from flask import Flask

DEBUG_ENABLED = False

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Yabadabadoo, I'm running inside a docker container</h1>"


if __name__ == '__main__':
    app.run(debug=DEBUG_ENABLED, host='0.0.0.0')