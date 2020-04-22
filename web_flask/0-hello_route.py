#!/usr/bin/python3
""" script that starts a Flask web application:
web application must be listening on 0.0.0.0, port 5000
Routes: /: display “Hello HBNB!”
must use the option strict_slashes=False in your route definition
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_world():
    """print Hello HBNB! """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
