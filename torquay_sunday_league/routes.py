from flask import render_template
from torquay_sunday_league import app, db
from torquay_sunday_league.models import Team, Player


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/teams")
def teams():
    return render_template("teams.html")


@app.route("/add_team", methods=["GET", "POST"])
def add_team():
    return render_template("add_team.html")