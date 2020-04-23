#!/usr/bin/python3
""" script that starts a Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000
    You must use storage for fetching data from the storage engine
    (FileStorage or DBStorage) => from models import storage and storage.all
    To load all cities of a State:
        If your storage engine is DBStorage, must use cities relationship
        Otherwise, use the public getter method cities
    After each request you must remove the current SQLAlchemy Session:
        Declare a method to handle @app.teardown_appcontext
        Call in this method storage.close()
    Routes:
        /cities_by_states: display a HTML page: (inside the tag BODY)
            H1 tag: “States”
            UL tag: with the list of all State objects present in DBStorage
            sorted by name (A->Z) tip
                LI tag: desc of one State: <state.id>: <B><state.name></B> +
                UL tag: list City objects linked to State sorted by name
                    LI tag: desc of one City: <city.id>: <B><city.name></B>
    Import this 7-dump to have some data
    You must use the option strict_slashes=False in your route definition
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    """ After each request you must remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/cities_by_states")
def cities_by_states():
    """display a HTML page: (inside the tag BODY)"""
    states = storage.all("State").values()
    cities = storage.all("City").values()
    return render_template('8-cities_by_states.html',
                           states=states, cities=cities)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
