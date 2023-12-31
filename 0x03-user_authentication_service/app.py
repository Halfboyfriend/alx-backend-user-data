#!/usr/bin/env python3
"""flask app for the auth service"""
from flask import Flask
from flask import (
    jsonify,
    abort,
    request
)
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def home() -> str:
    """home page for flask routes"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def register_user() -> str:
    """register users from form data"""
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": email, "message": "user created"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
