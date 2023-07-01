from flask import render_template
from torquay_sunday_league import app, db
from torquay_sunday_league.models import Team, Player


@app.route("/")
def home():
    return render_template("index.html")