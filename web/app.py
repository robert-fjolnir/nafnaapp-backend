from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Elska Ágústu svo mikið<h1>'


@app.route('/lol')
def lolol():
    return '<h1>Uhhhh, lolol<h1>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')