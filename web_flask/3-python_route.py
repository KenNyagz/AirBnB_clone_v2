#!/usr/bin/python3
'''starts a Flask web application
'''


from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    '''Defines landing page for root dir of web app'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''Defines another landing page to different path'''
    return 'HBNB'


@app.route('/c/')
@app.route('/c/<text>', strict_slashes=False)
def fun_is_c(text):
    '''Creates HTML http response for path taking argument'''
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def cool_is_py(text="is cool"):
    '''Creates HTML http response for path taking argument'''
    text = text.replace('_', ' ')
    return f"Python {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
