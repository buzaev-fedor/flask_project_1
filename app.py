import flask
from flask import Flask
from data import tours, title, subtitle, description, departures

app = Flask(__name__)


@app.route("/")
def main():
    return flask.render_template("index.html",
                                 tours=tours,
                                 title=title,
                                 subtitle=subtitle,
                                 description=description,
                                 departures=departures
                                 )


@app.route("/departures/<departure>/")
def render_departures(departure):
    tour_items = dict(filter(lambda tour: tour[1]["departure"] == departure, tours.items()))
    return flask.render_template("departure.html",
                                 subtitle=subtitle,
                                 title=title,
                                 departure=departure,
                                 tours=tour_items,
                                 departures=departures
                                 )


@app.route("/tours/<id>/")
def render_tours(id):
    id = int(id)
    return flask.render_template("tour.html",
                                 subtitle=subtitle,
                                 title=title,
                                 tour=tours[id],
                                 departures=departures
                                 )


@app.errorhandler(404)
def render_not_found(error):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"


@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим"


# # Бонусная часть
# @app.route("/data/")
# def data():
#     return flask.render_template("data.html",
#                                  tours=tours
#                                  )
#
#
# @app.route("/data/departures/<departure>")
# def get_departure(departure):
#     return flask.render_template("data_departure.html",
#                                  tours=tours,
#                                  departure=departure
#                                  )
#
#
# @app.route("/data/departures/<id>/")
# def get_id(id):
#     return flask.render_template("data_id.html",
#                                  tours=tours,
#                                  id2=int(id)
#                                  )


if __name__ == '__main__':
    app.run(debug=True)
