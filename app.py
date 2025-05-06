from flask import Flask, request


app = Flask(__name__)


@app.route("/some_route_here", methods=["GET"])
def method_name():
    return {}
