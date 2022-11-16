#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
    return 'Hello world!'

@app.route("/hello")
def hello():
    return "Hello"

@app.route("/hello/<name>")
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(debug = True)
