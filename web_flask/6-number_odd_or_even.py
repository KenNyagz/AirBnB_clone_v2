#!/usr/bin/python3
'''starts a Flask web application
'''


from flask import Flask, render_template


app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    '''Defines landing page for root dir of web app'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Defines another landing page to different path'''
    return 'HBNB'


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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    '''Creates HTML http response for path taking argument'''
    if isinstance(n, int):
        return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    '''Display a HTML page only if n is an integer'''
    if isinstance(n, int):
        odd_or_even = 'even' if n % 2 == 0 else 'odd'
        return render_template('6-number_odd_or_even.html', n=n,
                               odd_or_even=odd_or_even)


if __name__ == '__main__':
    '''runs the program as main module'''
    app.run(host='0.0.0.0', port=5000)
