#!/usr/bin/env python3

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def spec():
    data = {
        "data": "Hello World"
    }
    return jsonify(data)

app.run(host="0.0.0.0", port=8080)
