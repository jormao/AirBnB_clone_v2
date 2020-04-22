#!/usr/bin/python3
""" script that starts a Flask web application:
web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable
    /python/(<text>): display “Python ”, followed value of the text variable
        The default value of text is “is cool”
    number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer
        H1 tag: “Number: n” inside the tag BODY
must use the option strict_slashes=False in your route definition
"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_world():
    """print Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """print HBNB """
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """print C + text """
    text = text.replace("_", " ")
    return "C " + text


@app.route("/python/")
@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    """print Python + text """
    text = text.replace("_", " ")
    return "Python " + text


@app.route("/number/<int:n>")
def number_int(n):
    """print number is int """
    return str(n) + " is a number"


@app.route("/number_template/<int:n>")
def number_template_int(n):
    """display HTML page if n is integer """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """display HTML page only if n is an integer odd or even in the HTML"""
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
