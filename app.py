from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/hello")
def hello():
    return "hello"

@app.route("/name")
def name():
    return "pranjal"

@app.route("/surname")
def surname():
    return "shrivastava"

