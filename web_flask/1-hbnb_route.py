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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
