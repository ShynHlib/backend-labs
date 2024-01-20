from flask import Flask, jsonify
from datetime import date
from module import app

@app.route("/")
def homepage():
    response = "<p>Home page</p>"
    return response, 200

@app.route("/healthcheck")
def healthCheck():
    response = {
        'time': date.today(),
        'status': 200,
    }
    return jsonify(response), 200