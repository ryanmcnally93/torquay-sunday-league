from flask import render_template, request, redirect, url_for, flash, session
from sqlalchemy import exc
from torquay_sunday_league import app, db
from torquay_sunday_league.models import Team, Player, User
from werkzeug.security import generate_password_hash, check_password_hash
import datetime


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/teams")
def teams():
    teams = list(Team.query.order_by(Team.team_name).all())
    # update team no of players
    return render_template("teams.html", teams=teams)


@app.route("/create_team", methods=["GET", "POST"])
def create_team():
    if request.method == "POST":
        team = Team(
            team_name=request.form.get("team_name"),
            team_no_of_players=0,
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
        emailaddress = request.form.get("emailaddress")
        password = generate_password_hash(request.form.get("password"))

        # Check username doesn't exist
        user_object = User.query.filter_by(username=username).first()
        if user_object:
            return "This username is taken!"

        # Check email doesn't exist
        email_object = User.query.filter_by(emailaddress=emailaddress).first()
        if email_object:
            return "This email address is taken!"

        # Get the month and year of registration
        date_time = datetime.datetime.now()
        month = date_time.strftime("%B")
        year = date_time.year
        month_joined = "%s %s" % (month, year)
        user = User(username=username, password=password, emailaddress=emailaddress, month_joined=month_joined)
        db.session.add(user)
        db.session.commit()

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    username = request.form.get("username")
    if request.method == "POST":
        # Check that the user exists
        user_object = User.query.filter_by(username=username).first()
        if user_object:
            # Check password is a match
            # # if check_password_hash(
            # #     # THIS LINE IS A MISTAKE I HAD!!!!
            # #     user_object["password"], request.form.get("password")):
            if check_password_hash(user_object.password, request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # Invalid password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("log_in"))
                
        else:
            # Invalid username
            flash("Incorrect Username and/or Password")
            return redirect(url_for("log_in"))

    return render_template("log_in.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    user = User.query.filter_by(username=username).first()
    username = session["user"]

    # Checking for session cookie
    if session["user"]:
        return render_template("user_profile.html", username=username, user=user)
    
    # If no session cookie, we return to log_in page
    return redirect(url_for("log_in"))


@app.route("/log_out")
def log_out():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("log_in"))


@app.route("/edit_team/<int:team_id>", methods=["GET", "POST"])
def edit_team(team_id):
    team = Team.query.get_or_404(team_id)
    if request.method == "POST":
        team.team_name = request.form.get("team_name")
        team.team_no_of_players = len(Player.query.get(team_id))
        team.team_colour = request.form.get("team_colour")
        team.team_location = request.form.get("team_location")
        db.session.commit()
        # Change redirect for team profile page
        return redirect(url_for("teams"))
    return render_template("edit_team.html", team=team)


@app.route("/delete_team/<int:team_id>")
def delete_team(team_id):
    team = Team.query.get_or_404(team_id)
    db.session.delete(team)
    db.session.commit()
    return redirect(url_for("teams"))


@app.route("/players/<int:id>")
def players(id):
    team = Team.query.get_or_404(id)
    players = list(Player.query.order_by(Player.player_kit_number).all())
    return render_template("players.html", players=players, team=team)


@app.route("/edit_player/<int:player_id>/<int:team_id>", methods=["GET", "POST"])
def edit_player(player_id, team_id):
    player = Player.query.get_or_404(player_id)
    teams = list(Team.query.order_by(Team.team_name).all())
    team = Team.query.get_or_404(team_id)
    if request.method == "POST":
        player.player_kit_number=request.form.get("player_kit_number")
        player.player_name = request.form.get("player_name")
        player.player_country = request.form.get("player_country")
        player.player_position = request.form.get("player_position")
        player.player_joined = request.form.get("player_joined")
        db.session.commit()
        players = list(Player.query.order_by(Player.player_kit_number).all())
        return render_template("players.html", players=players, team=team)
    return render_template("edit_player.html", player=player, team=team, teams=teams)


@app.route("/add_player/<int:id>", methods=["GET", "POST"])
def add_player(id):
    players = list(Player.query.order_by(Player.player_kit_number).all())
    search = Team.query.get(id).players
    teams = list(Team.query.order_by(Team.team_name).all())
    team = Team.query.get_or_404(id)
    for current in search:
        if str(current.player_kit_number) == request.form.get("player_kit_number"):
            flash(f"Error: This {team.team_name} kit number is already taken!")
            return render_template("add_player.html", teams=teams, team=team,)

    for current in search:
        if str(current.player_name) == request.form.get("player_name"):
            flash(f"Error: This player has already been registered!")
            return render_template("add_player.html", teams=teams, team=team,)
    
    if request.method == "POST":
        player = Player(
            player_kit_number=int(request.form.get("player_kit_number")),
            player_name=request.form.get("player_name"),
            player_position=request.form.get("player_position"),
            player_joined=request.form.get("player_joined"),
            player_country=request.form.get("player_country"),
            team_id=request.form.get("team_id")
        )

        db.session.add(player)
        db.session.commit()
        
        players = list(Player.query.order_by(Player.player_kit_number).all())
        return render_template("players.html", players=players, team=team)

    return render_template("add_player.html", teams=teams, team=team)


@app.route("/team_profile/<int:id>", methods=["GET", "POST"]) 
def team_profile(id):
    team = Team.query.get_or_404(id)
    number_of_players = 0
    players = Team.query.get(id).players
    for player in players:
        number_of_players += 1

    team.team_no_of_players = number_of_players
    if number_of_players < 16:
        flash("You must have 16 players to be accepted")
    return render_template("team_profile.html", team=team)


@app.route("/delete_player/<int:team_id>/<int:player_id>")
def delete_player(team_id, player_id):
    player = Player.query.get_or_404(player_id)
    team = Team.query.get_or_404(team_id)
    db.session.delete(player)
    db.session.commit()
    players = list(Player.query.order_by(Player.player_kit_number).all())
    return render_template("players.html", players=players, team=team)


@app.route("/user_edit/<username>", methods=["GET", "POST"])
def user_edit(username):
    user = User.query.filter_by(username=username).first()
    if request.method == "POST":
        user.emailaddress = request.form.get("emailaddress")
        user.password = generate_password_hash(request.form.get("password"))
        db.session.commit()
        return render_template("user_profile.html", user=user)
    return render_template("user_edit.html", user=user)