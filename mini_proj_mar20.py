# mini_proj_mar20.py

import math
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/name", methods=["GET"])
def name():
    name_info = {
      "name": "Connor"
    }
    return jsonify(name_info)


@app.route("/hello/<name>", methods=["GET"])
def hello_name(name):
	hello_message = {
	    "message": "Hello there, {}".format(name)
	}
	return jsonify(hello_message)


@app.route("/distance", methods=["POST"])
def distance():
    r = request.get_json() # parses the POST request body as JSON
    a = r["a"]
    b = r["b"]
    dist = find_dist(a,b)
    dist_output = {
      "distance": dist,
      "a": a,
      "b": b
    }
    return jsonify(dist_output)


def find_dist(a,b):
    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]
    dist = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return dist


if __name__ == '__main__':
    app.run()