from flask import render_template, request, redirect, url_for, flash, session
from sqlalchemy import exc
from torquay_sunday_league import app, db
from torquay_sunday_league.models import Team, Player, User
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


@app.route("/")
def home():
    if session:
        user1 = User.query.filter_by(username=session["user"]).first()
        team1 = Team.query.filter_by(team_name=user1.team_managed).first()
        return render_template("index.html", user=user1, team=team1)
    else:
        user1 = "None"
        team1 = "None"
    return render_template("index.html", user=user1, team=team1)


@app.route("/teams")
def teams():
    if session:
        user1 = User.query.filter_by(username=session["user"]).first()
        team1 = Team.query.filter_by(team_name=user1.team_managed).first()
    else:
        user1 = "None"
        team1 = "None"

    teams = list(Team.query.order_by(Team.team_name).all())
    # update team no of players
    return render_template("teams.html", teams=teams, user=user1, team=team1)


@app.route("/create_team/<username>", methods=["GET", "POST"])
def create_team(username):
    user = User.query.filter_by(username=username).first()
    if request.method == "POST":
        if session["user"] == "ryanmcnally93" or user.team_managed == "None":
            team = Team(
                team_name=request.form.get("team_name"),
                team_no_of_players=0,
                team_colour=request.form.get("team_colour"),
                team_location=request.form.get("team_location"),
                team_created_by=session["user"]
                )
            user.team_managed = team.team_name
            db.session.add(team)
            db.session.commit()
            return redirect(url_for("teams", username=session["user"], user=user))
        else:
            flash("A user may only register one team.")
    return render_template("create_team.html", username=session["user"], user=user)


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
        date_time = datetime.now()
        month = date_time.strftime("%B")
        year = date_time.year
        month_joined = "%s %s" % (month, year)
        user = User(
            username=username,
            password=password,
            emailaddress=emailaddress,
            month_joined=month_joined,
            team_managed="None"
            )
        db.session.add(user)
        db.session.commit()

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("create_team", username=session["user"], user=user))
    return render_template("register.html")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    username = request.form.get("username")
    if request.method == "POST":
        # Check that the user exists
        user_object = User.query.filter_by(username=username).first()
        if user_object:
            if check_password_hash(user_object.password, request.form.get("password")):
                user = User.query.filter_by(username=username).first()
                team1 = Team.query.filter_by(team_name=user.team_managed).first()
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"], user=user, team=team1))
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
    team1 = Team.query.filter_by(team_name=user.team_managed).first()
    username = session["user"]

    # Checking for session cookie
    if session["user"]:
        return render_template("user_profile.html", username=username, user=user, team=team1)
    
    # If no session cookie, we return to log_in page
    return redirect(url_for("log_in", username=username, user=user, team=team1))


@app.route("/log_out")
def log_out():
    user = session["user"]
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("log_in"))


@app.route("/edit_team/<int:team_id>", methods=["GET", "POST"])
def edit_team(team_id):
    user1 = User.query.filter_by(username=session["user"]).first()
    team = Team.query.get_or_404(team_id)
    if request.method == "POST":
        if session["user"] == team.team_created_by:
            team.team_name = request.form.get("team_name")
            team.team_colour = request.form.get("team_colour")
            team.team_location = request.form.get("team_location")
            user1.team_managed = team.team_name
            db.session.commit()
            # Change redirect for team profile page
            return redirect(url_for("teams", user=user1))
        else:
            flash("Only the creator of this team may edit it.")
    return render_template("edit_team.html", team=team, user=user1)


@app.route("/delete_team/<int:team_id>")
def delete_team(team_id):
    team = Team.query.get_or_404(team_id)
    user1 = User.query.filter_by(username=session["user"]).first()
    if session["user"] == team.team_created_by:
        user1.team_managed = "None"
        db.session.delete(team)
        db.session.commit()
        return redirect(url_for("teams", user=user1))
    else:
        flash("Only the creator of this team may delete it.")


@app.route("/players/<int:id>")
def players(id):
    user1 = User.query.filter_by(username=session["user"]).first()
    team = Team.query.get_or_404(id)
    players = list(Player.query.order_by(Player.player_kit_number).all())
    return render_template("players.html", players=players, team=team, user=user1)


@app.route("/edit_player/<int:player_id>/<int:team_id>", methods=["GET", "POST"])
def edit_player(player_id, team_id):
    user1 = User.query.filter_by(username=session["user"]).first()
    player = Player.query.get_or_404(player_id)
    teams = list(Team.query.order_by(Team.team_name).all())
    team = Team.query.get_or_404(team_id)
    if request.method == "POST":
        if session["user"] == team.team_created_by:
            player.player_kit_number=request.form.get("player_kit_number")
            player.player_name = request.form.get("player_name")
            player.player_country = request.form.get("player_country")
            player.player_position = request.form.get("player_position")
            player.player_joined = request.form.get("player_joined")
            db.session.commit()
            players = list(Player.query.order_by(Player.player_kit_number).all())
            return render_template("players.html", players=players, team=team, user=user1)
        else:
            flash("Only the creator of this team may edit its players.")
    return render_template("edit_player.html", player=player, team=team, teams=teams, user=user1)


@app.route("/add_player/<int:id>", methods=["GET", "POST"])
def add_player(id):
    if session:
        user1 = User.query.filter_by(username=session["user"]).first()
        team = Team.query.get_or_404(id)
    else:
        user1 = "None"
        team1 = "None"

    players = list(Player.query.order_by(Player.player_kit_number).all())
    search = Team.query.get(id).players
    teams = list(Team.query.order_by(Team.team_name).all())
    for current in search:
        if str(current.player_kit_number) == request.form.get("player_kit_number"):
            flash(f"Error: This {team.team_name} kit number is already taken!")
            return render_template("add_player.html", teams=teams, team=team, user=user1)

    for current in search:
        if str(current.player_name) == request.form.get("player_name"):
            flash(f"Error: This player has already been registered!")
            return render_template("add_player.html", teams=teams, team=team, user=user1)
    
    if request.method == "POST":
        if session["user"] == team.team_created_by:
            player = Player(
                player_kit_number=int(request.form.get("player_kit_number")),
                player_name=request.form.get("player_name"),
                player_position=request.form.get("player_position"),
                player_joined=request.form.get("player_joined"),
                player_country=request.form.get("player_country"),
                team_id=team.id
            )
            arrival = datetime.strptime(player.player_joined, "%d/%m/%Y")
            present = datetime.now()
            if present.date() < arrival.date():
                flash("If this player hasn't officially joined he cannot be submitted")
                return render_template("players.html", players=players, team=team, user=user1)

            db.session.add(player)
            db.session.commit()
            players = list(Player.query.order_by(Player.player_kit_number).all())
            return render_template("players.html", players=players, team=team, user=user1)
        else:
            flash("Only the creator of this team may add players to it.")

    return render_template("add_player.html", teams=teams, team=team, user=user1)


@app.route("/team_profile/<int:id>", methods=["GET", "POST"]) 
def team_profile(id):
    user1 = User.query.filter_by(username=session["user"]).first()
    team = Team.query.get_or_404(id)
    number_of_players = 0
    players = Team.query.get(id).players
    for player in players:
        number_of_players += 1

    team.team_no_of_players = number_of_players
    if number_of_players < 16 and session["user"] != "ryanmcnally93":
        flash("You must have 16 players to be accepted")
    return render_template("team_profile.html", team=team, user=user1)


@app.route("/delete_player/<int:team_id>/<int:player_id>")
def delete_player(team_id, player_id):
    user1 = User.query.filter_by(username=session["user"]).first()
    player = Player.query.get_or_404(player_id)
    team = Team.query.get_or_404(team_id)
    if session["user"] == team.team_created_by:
        db.session.delete(player)
        db.session.commit()
        players = list(Player.query.order_by(Player.player_kit_number).all())
        return render_template("players.html", players=players, team=team, user=user1)
    else:
        flash("Only the creator of this team may delete its players.")


@app.route("/user_edit/<username>", methods=["GET", "POST"])
def user_edit(username):
    user = User.query.filter_by(username=username).first()
    team1 = Team.query.filter_by(team_name=user.team_managed).first()
    if session["user"] == "ryanmcnally93":
        flash("WARNING Changing your email address will affect your admin status.")

    if request.method == "POST":
        user.emailaddress = request.form.get("emailaddress")
        user.password = generate_password_hash(request.form.get("password"))
        db.session.commit()
        return render_template("user_profile.html", user=user, team=team1)
    return render_template("user_edit.html", user=user, team=team1)