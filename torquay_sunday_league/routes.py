from flask import render_template, request, redirect, url_for
from torquay_sunday_league import app, db
from torquay_sunday_league.models import Team, Player, User


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/teams")
def teams():
    teams = Team.query.order_by(Team.team_name).all()
    return render_template("teams.html", teams=teams)


@app.route("/create_team", methods=["GET", "POST"])
def create_team():
    if request.method == "POST":
        team = Team(
            team_name=request.form.get("team_name"),
            team_no_of_players=request.form.get("team_no_of_players"),
            team_colour=request.form.get("team_colour"),
            team_location=request.form.get("team_location")
            )
        db.session.add(team)
        db.session.commit()
        return redirect(url_for("teams"))
    return render_template("create_team.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Check username exists
        user_object = User.query.filter_by(username=username).first()
        if user_object:
            return "This username is taken!"

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return "Inserted into DB!"

    return render_template("register.html")