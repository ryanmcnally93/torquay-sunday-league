from flask import render_template, request, redirect, url_for
from torquay_sunday_league import app, db
from torquay_sunday_league.models import Team, Player


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/teams")
def teams():
    return render_template("teams.html")


@app.route("/create_team", methods=["GET", "POST"])
def create_team():
    if request.method == "POST":
        team = Team(team_name=request.form.get("team_name"))
        db.session.add(team)
        db.session.commit()
        return redirect(url_for("teams"))
    return render_template("create_team.html")