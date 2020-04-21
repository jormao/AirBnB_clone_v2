#!/usr/bin/python3
""" script that starts a Flask web application:
web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space)
must use the option strict_slashes=False in your route definition
"""
from flask import Flask
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

if __name__ == "__main__":
    app.run(debug=True)
