from flask import render_template, request, abort, jsonify, send_from_directory
from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/favicon.ico")
def favicon():
    return send_from_directory("static", "favicon.ico")