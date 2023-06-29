from flask import render_template
from torquay_super_league import app, db


@app.route("/")
def home():
    return render_template("base.html")