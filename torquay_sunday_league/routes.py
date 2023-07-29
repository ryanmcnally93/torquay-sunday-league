import os
import secrets
from PIL import Image
from flask import render_template, request, redirect, url_for, flash, session
from sqlalchemy import exc
from torquay_sunday_league import app, db
from torquay_sunday_league.models import Team, Player, User
from torquay_sunday_league.models import (
    UpdateProfilePicture, UpdateTeamPicture)
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import requests
from pprint import pprint
import json


# Homepage
@app.route("/")
def home():
    # Log in check, to display correct navbar information
    if "user" in session:
        user1 = User.query.filter_by(username=session["user"]).first()
        team1 = Team.query.filter_by(team_name=user1.team_managed).first()
        profile_picture = url_for(
            'static', filename='images/profile_pics/' + user1.profile_picture)
    else:
        # Set to none if not logged in
        user1 = "None"
        team1 = "None"
        profile_picture = "None"

    # Teams is needed to display them in the table
    teams = list(Team.query.order_by(Team.team_name).all())
    return render_template("index.html", user=user1, team=team1, teams=teams, profile_picture=profile_picture)


# Teams Page
@app.route("/teams", methods=["GET", "POST"])
def teams():
    # Log in check, to display correct navbar information
    if "user" in session:
        user1 = User.query.filter_by(username=session["user"]).first()
        baseteam = Team.query.filter_by(team_name=user1.team_managed).first()
        profile_picture = url_for(
            'static', filename='images/profile_pics/' + user1.profile_picture)
        currentteam = "None"

        # This code runs when the form is submitted
        if request.method == "POST":
            currentteam = Team.query.filter_by(
                team_name=request.form.get("teamid")).first()
            currentteam.confirmation_status = bool(
                True if request.form.get(f"{ currentteam.id }confirmed") else False)
            db.session.commit()
            flash("Confirmation changed")
    else:
        # This information is set for users not logged in
        user1 = "None"
        baseteam = "None"
        profile_picture = "None"
        currentteam = "None"

    # Teams is needed for team cards
    teams = list(Team.query.order_by(Team.team_name).all())
    title = "Teams"
    return render_template("teams.html", teams=teams, user=user1, team=baseteam, profile_picture=profile_picture, title=title)


# Rules Page
@app.route("/rules")
def rules():
    # Log in check, to display correct navbar information
    if "user" in session:
        user1 = User.query.filter_by(username=session["user"]).first()
        team1 = Team.query.filter_by(team_name=user1.team_managed).first()
        profile_picture = url_for(
            'static', filename='images/profile_pics/' + user1.profile_picture)
    else:
        # If user is not logged in, variables set to None
        user1 = "None"
        team1 = "None"
        profile_picture = "None"
    title = "rules"
    return render_template("rules.html", user=user1, team=team1, profile_picture=profile_picture, title=title)


# Create Team Page
@app.route("/create_team/<username>", methods=["GET", "POST"])
def create_team(username):
    # These links identify the user, team and profile image
    user = User.query.filter_by(username=username).first()
    team1 = Team.query.filter_by(team_name=user.team_managed).first()
    profile_picture = url_for(
        'static', filename='images/profile_pics/' + user.profile_picture)

    # Log in check, to display correct navbar information
    if "user" in session:
        if session["user"] != username:
            flash("You cannot create a team as another manager.")
            return redirect(url_for("user_profile", username=session["user"]))

        # This code runs when the form is submitted
        if request.method == "POST":
            if session["user"] == "ryanmcnally93" or user.team_managed == "None":
                team = Team(
                    team_name=request.form.get("team_name"),
                    team_no_of_players=0,
                    team_colour=request.form.get("team_colour"),
                    team_location=request.form.get("team_location"),
                    team_contact=request.form.get("team_contact"),
                    confirmation_status=bool(False),
                    team_created_by=session["user"],
                    users_id=user.id
                )

                # Check to see if the team name is taken
                team_name = Team.query.filter_by(
                    team_name=team.team_name).first()
                if team_name:
                    flash("This team name is taken!")
                    return redirect(url_for("create_team", username=session["user"]))

                # Set the team managed status for user
                user.team_managed = team.team_name
                # Team added to database
                db.session.add(team)
                db.session.commit()
                return redirect(url_for("teams"))
            else:
                # This is for managers who already have a team
                flash("A user may only register one team.")

    else:
        # This is for users not logged in
        flash("You are not logged in.")
        return redirect(url_for("log_in"))

    title = "Create Team"
    return render_template("create_team.html", username=session["user"], user=user, team=team1, profile_picture=profile_picture, title=title)


# Register Page
@app.route("/register", methods=["GET", "POST"])
def register():
    # Log in check, to display correct navbar information
    if "user" in session:
        flash("You are logged in.")
        return redirect(url_for("user_profile", username=session["user"]))

    # This code runs when the form is submitted
    if request.method == "POST":
        username = request.form.get("username").lower()
        emailaddress = request.form.get("emailaddress").lower()
        password = generate_password_hash(request.form.get("password"))

        # This code runs if the password don't match
        if request.form.get("password") != request.form.get("confirm_password"):
            flash("ERROR! Your passwords do not match")
            return redirect(url_for("register"))

        # Check username doesn't exist
        user_object = User.query.filter_by(username=username).first()
        if user_object:
            flash("Username is taken")
            return redirect(url_for("register"))

        # Check email doesn't exist
        email_object = User.query.filter_by(emailaddress=emailaddress).first()
        if email_object:
            flash("Email address is taken")
            return redirect(url_for("register"))

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

        # Steps to take when administrator registers account
        if username == "ryanmcnally93":
            session["user"] = request.form.get("username").lower()
            flash("Registration Successful!")
            return redirect(url_for("user_profile", username=session["user"]))

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("create_team", username=session["user"]))

    title = "Register"
    return render_template("register.html", title=title)


# Log In Page
@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    # Log in check, to display correct navbar information
    if "user" in session:
        flash("You are logged in.")
        return redirect(url_for("user_profile", username=session["user"]))

    username = request.form.get("username")
    # This code runs when the form is submitted
    if request.method == "POST":
        # Check that the user exists
        user_object = User.query.filter_by(username=username).first()
        if user_object:
            if check_password_hash(user_object.password, request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("user_profile", username=session["user"]))
            else:
                # Invalid password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("log_in"))

        else:
            # Invalid username
            flash("Incorrect Username and/or Password")
            return redirect(url_for("log_in"))

    title = "Log In"
    return render_template("log_in.html", title=title)


# User Profile Page
@app.route("/user_profile/<username>", methods=["GET", "POST"])
def user_profile(username):
    # Log in check, to display correct navbar information
    if "user" in session:
        user = User.query.filter_by(username=username).first()
        team1 = Team.query.filter_by(team_name=user.team_managed).first()
        profile_picture = url_for(
            'static', filename='images/profile_pics/' + user.profile_picture)

    else:
        # This code runs if the user is not logged in
        flash("You are not logged in.")
        return redirect(url_for("log_in"))

    title = "User Profile"
    return render_template("user_profile.html", username=username, user=user, profile_picture=profile_picture, team=team1, title=title)


# Log Out Function, returns user to log in page
@app.route("/log_out")
def log_out():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("log_in"))


# Edit Team Page
@app.route("/edit_team/<int:team_id>", methods=["GET", "POST"])
def edit_team(team_id):
    # Log in check, to display correct navbar information
    if "user" in session:
        currentteam = Team.query.get_or_404(team_id)
        if session["user"] != currentteam.team_created_by:
            # Code to stop users being able to make changes to another managers team
            flash("You cannot edit a team that is not yours.")
            return redirect(url_for("user_profile", username=session["user"]))

        # Set these variables for the navbar to function and information to display
        user1 = User.query.filter_by(username=session["user"]).first()
        baseteam = Team.query.filter_by(team_name=user1.team_managed).first()
        squad_picture = url_for(
            'static', filename='images/profile_pics/' + currentteam.profile_picture)
        profile_picture = url_for(
            'static', filename='images/profile_pics/' + user1.profile_picture)
        form = UpdateTeamPicture()

        # This code runs when the form is submitted
        if request.method == "POST":
            if form.validate_on_submit():
                flash("Validated!")

            # Checks for errors in the form
            if form.picture.errors:
                return render_template("edit_team.html", currentteam=currentteam, team=baseteam, user=user1, squad_picture=squad_picture, form=form)

            if form.picture.data:
                # Deletes last image
                if currentteam.profile_picture != 'default_squad.webp':
                    os.remove(os.path.join(app.root_path,
                                           'static/images/profile_pics', currentteam.profile_picture))

                # Setting new profile image
                picture_file = save_picture(form.picture.data, 2)
                currentteam.profile_picture = picture_file
                db.session.commit()
                squad_picture = url_for(
                    'static', filename='images/profile_pics/' + currentteam.profile_picture)
                flash("Squad picture changed")

            if session["user"] == currentteam.team_created_by:
                team_name_search_positive = Team.query.filter_by(
                    team_name=request.form.get("team_name")).first()
                if team_name_search_positive:
                    # Checks for taken username
                    if currentteam.team_name != request.form.get("team_name"):
                        flash("This team name is taken!")
                        return render_template("edit_team.html", team=baseteam, currentteam=currentteam, user=user1, squad_picture=squad_picture, form=form)

                # Setting new team information
                currentteam.team_name = request.form.get("team_name")
                currentteam.team_colour = request.form.get("team_colour")
                currentteam.team_location = request.form.get("team_location")
                currentteam.team_contact = request.form.get("team_contact")

                user1.team_managed = currentteam.team_name
                db.session.commit()
                flash("Team data changed")
                return redirect(url_for("team_profile", id=currentteam.id))
            else:
                # Runs if a different manager gets to this stage
                flash("Only the creator of this team may edit it.")
    else:
        # If the user is not logged in
        flash("You are not logged in.")
        return redirect(url_for("log_in"))

    title = "Edit Team"
    return render_template("edit_team.html", team=baseteam, currentteam=currentteam, user=user1, squad_picture=squad_picture, form=form, profile_picture=profile_picture, title=title)


# Delete Team Function, returns user to teams page
# This function will cascade and delete the teams players
@app.route("/delete_team/<int:team_id>")
def delete_team(team_id):
    # Log in check, to display correct navbar information
    if "user" in session:
        team = Team.query.get_or_404(team_id)
        user1 = User.query.filter_by(username=session["user"]).first()
        # Checks you are the creator
        if session["user"] == team.team_created_by:
            user1.team_managed = "None"
            db.session.delete(team)
            db.session.commit()
            return redirect(url_for("teams"))
        else:
            flash("Only the creator of this team may delete it.")
            return redirect(url_for("teams"))
    else:
        # If the user is not logged in
        flash("You are not logged in.")
        return redirect(url_for("log_in"))


# Players Page
@app.route("/players/<int:id>")
def players(id):
    # Log in check, to display correct navbar information
    if "user" in session:
        user1 = User.query.filter_by(username=session["user"]).first()
        baseteam = Team.query.filter_by(team_name=user1.team_managed).first()
        profile_picture = url_for(
            'static', filename='images/profile_pics/' + user1.profile_picture)
    else:
        # If you are not logged in
        user1 = "None"
        baseteam = "None"
        profile_picture = "None"

    # Setting variables for team and players
    currentteam = Team.query.get_or_404(id)
    players = list(Player.query.order_by(Player.player_kit_number).all())
    title = "Players"
    return render_template("players.html", players=players, team=baseteam, user=user1, currentteam=currentteam, profile_picture=profile_picture, title=title)


# Edit Player Page
@app.route("/edit_player/<int:player_id>/<int:team_id>", methods=["GET", "POST"])
def edit_player(player_id, team_id):
    # Log in check, to display correct navbar information
    if "user" in session:
        currentteam = Team.query.get_or_404(team_id)
        if session["user"] != currentteam.team_created_by:
            flash("You cannot edit someone elses player.")
            return redirect(url_for("user_profile", username=session["user"]))

        # Setting variables for player, team and profile picture
        user1 = User.query.filter_by(username=session["user"]).first()
        player = Player.query.get_or_404(player_id)
        baseteam = Team.query.filter_by(team_name=user1.team_managed).first()
        profile_picture = url_for(
            'static', filename='images/profile_pics/' + user1.profile_picture)
        teams = list(Team.query.order_by(Team.team_name).all())

        # Check to see if the team has another player with this kit number
        search = Team.query.get(team_id).players
        for current in search:
            if str(current.player_name) != player.player_name:
                if str(current.player_kit_number) == request.form.get("player_kit_number"):
                    flash(
                        f"Error: This {currentteam.team_name} kit number is already taken!")
                    return render_template("edit_player.html", player=player, team=baseteam, currentteam=currentteam, teams=teams, user=user1)

        # Check to see if this team has another player with the same name
        for current in search:
            if str(current.player_name) != player.player_name:
                if str(current.player_name) == request.form.get("player_name"):
                    flash("Error: This player has already been registered!")
                    return render_template("edit_player.html", player=player, team=baseteam, currentteam=currentteam, teams=teams, user=user1)

        # This code only runs when the form is submitted
        if request.method == "POST":
            if session["user"] == currentteam.team_created_by:
                player.player_kit_number = request.form.get(
                    "player_kit_number")
                player.player_name = request.form.get("player_name")
                player.player_country = request.form.get("player_country")
                player.player_position = request.form.get("player_position")
                db.session.commit()
                players = list(Player.query.order_by(
                    Player.player_kit_number).all())
                return redirect(url_for("players", id=team_id))
            else:
                # Check to see if you are the creator
                flash("Only the creator of this team may edit its players.")
    else:
        # If you are not logged in
        flash("You are not logged in.")
        return redirect(url_for("log_in"))

    title = "Edit Player"
    return render_template("edit_player.html", player=player, team=baseteam, currentteam=currentteam, teams=teams, user=user1, profile_picture=profile_picture, title=title)


# Add Player Page
@app.route("/add_player/<int:id>", methods=["GET", "POST"])
def add_player(id):
    # Log in check, to display correct navbar information
    if "user" in session:
        currentteam = Team.query.get_or_404(id)
        if session["user"] != currentteam.team_created_by:
            flash("You cannot add a player to someone elses team.")
            return redirect(url_for("user_profile", username=session["user"]))

        # Setting variables for the page
        user1 = User.query.filter_by(username=session["user"]).first()
        profile_picture = url_for(
            'static', filename='images/profile_pics/' + user1.profile_picture)
        baseteam = Team.query.filter_by(team_name=user1.team_managed).first()
        search = Team.query.get(id).players
        teams = list(Team.query.order_by(Team.team_name).all())

        # Check to see if the team has another player with this kit number
        for current in search:
            if str(current.player_kit_number) == request.form.get("player_kit_number"):
                flash(
                    f"Error: This {currentteam.team_name} kit number is already taken!")
                return render_template("add_player.html", teams=teams, team=baseteam, currentteam=currentteam, user=user1)

        # Check to see if the team has another player with this name
        for current in search:
            if str(current.player_name) == request.form.get("player_name"):
                flash("Error: This player has already been registered!")
                return render_template("add_player.html", teams=teams, team=baseteam, currentteam=currentteam, user=user1)

        # This code only runs when the form is submitted
        if request.method == "POST":
            if session["user"] == currentteam.team_created_by:
                if request.form.get("player_joined") == "":
                    flash("You must enter the player join date")
                    return redirect(url_for("add_player", id=id))

                # Set information for player
                player = Player(
                    player_kit_number=int(
                        request.form.get("player_kit_number")),
                    player_name=request.form.get("player_name"),
                    player_position=request.form.get("player_position"),
                    player_joined=request.form.get("player_joined"),
                    player_country=request.form.get("player_country"),
                    team_id=currentteam.id
                )

                # Checks to see if the date is in the past
                arrival = datetime.strptime(player.player_joined, "%d/%m/%Y")
                present = datetime.now()
                if present.date() < arrival.date():
                    flash(
                        "If this player hasn't officially joined he cannot be submitted")
                    return redirect(url_for("add_player", id=id))

                # Adding player to database and increasing teams no. of players
                currentteam.team_no_of_players += 1
                db.session.add(player)
                db.session.commit()
                return redirect(url_for("players", id=id))
            else:
                # If the user is not the creator
                flash("Only the creator of this team may add players to it.")
    else:
        # If you are not logged in
        flash("You are not logged in.")
        return redirect(url_for("log_in"))

    title = "Add Player"
    return render_template("add_player.html", teams=teams, team=baseteam, currentteam=currentteam, user=user1, profile_picture=profile_picture, title=title)


# Team Profile Page
@app.route("/team_profile/<int:id>", methods=["GET", "POST"])
def team_profile(id):
    # Log in check, to display correct navbar information
    if "user" in session:
        user1 = User.query.filter_by(username=session["user"]).first()
        baseteam = Team.query.filter_by(team_name=user1.team_managed).first()
        profile_picture = url_for(
            'static', filename='images/profile_pics/' + user1.profile_picture)
    else:
        # If you are not logged in
        user1 = "None"
        baseteam = "None"
        profile_picture = "None"

    # If the number of player is under 16
    currentteam = Team.query.get_or_404(id)
    if "user" in session:
        if currentteam.team_no_of_players < 16 and session["user"] != "ryanmcnally93" and session["user"] == currentteam.team_created_by:
            flash("You must have 16 players to be accepted")

    # For squad picture
    squad_picture = url_for(
        'static', filename='images/profile_pics/' + currentteam.profile_picture)
    title = "Team Profile"
    return render_template("team_profile.html", currentteam=currentteam, team=baseteam, user=user1, squad_picture=squad_picture, profile_picture=profile_picture, title=title)


# Delete Player function, returns user to players page
@app.route("/delete_player/<int:team_id>/<int:player_id>")
def delete_player(team_id, player_id):
    # Log in check, to display correct navbar information
    if "user" in session:
        player = Player.query.get_or_404(player_id)
        team = Team.query.get_or_404(team_id)
        # Checks to see if you are the creator
        if session["user"] == team.team_created_by:
            team.team_no_of_players -= 1
            db.session.delete(player)
            db.session.commit()
            return redirect(url_for("players", id=team_id))
        else:
            flash("Only the creator of this team may delete its players.")
            return redirect(url_for("players", id=team_id))
    else:
        # If you are not logged in
        flash("You are not logged in.")
        return redirect(url_for("log_in"))


# Save Picture Function, for profile pictures
def save_picture(form_picture, x):
    # This randomises the file name so 2 files can be uploaded with the same name
    random_hex = secrets.token_hex(8)
    # This gets the file extension type
    _, f_ext = os.path.splitext(form_picture.filename)
    # This creates a new filename
    picture_fn = random_hex + f_ext
    # Location of file save
    picture_path = os.path.join(
        app.root_path, 'static/images/profile_pics', picture_fn)

    # For user profile
    if x == 1:
        im = Image.open(form_picture)
        im.thumbnail((316, 500))
    else:
        # For team profile
        im = Image.open(form_picture)
        im.thumbnail((316, 316))

    # Image saves
    im.save(picture_path)

    return picture_fn


# Edit User Page
@app.route("/user_edit/<username>", methods=["GET", "POST"])
def user_edit(username):
    # Log in check, to display correct navbar information
    if "user" in session:
        user = User.query.filter_by(username=username).first()
        team1 = Team.query.filter_by(team_name=user.team_managed).first()
        profile_picture = url_for(
            'static', filename='images/profile_pics/' + user.profile_picture)
        form = UpdateProfilePicture()

        # This if statement stops the user from being able
        # to type another managers name into the URL and make changes.
        if session["user"] != username:
            flash("You cannot change the details of another user.")
            return redirect(url_for("user_profile", username=session["user"]))

        # This code runs when the form is submitted
        if request.method == "POST":
            if form.validate_on_submit():
                flash("Validated!")

            # Checking for errors
            if form.picture.errors:
                return render_template("user_edit.html", user=user, team=team1, profile_picture=profile_picture, form=form)

            if form.picture.data:
                # Deletes last image
                if user.profile_picture != 'default_manager.webp':
                    os.remove(os.path.join(app.root_path,
                                           'static/images/profile_pics', user.profile_picture))
                current = request.form.get("confirm_password")
                # This code checks that the password is correct
                if check_password_hash(user.password, current):
                    if request.form.get("emailaddress") == "" or request.form.get("emailaddress") == user.emailaddress:
                        # When changing picture only
                        if request.form.get("password") == "":
                            picture_file = save_picture(form.picture.data, 1)
                            user.profile_picture = picture_file
                            db.session.commit()
                            profile_picture = url_for(
                                'static', filename='images/profile_pics/' + user.profile_picture)
                            flash("Profile picture changed")
                            return redirect(url_for("user_profile", username=username))
                        # When Changing picture and password
                        else:
                            picture_file = save_picture(form.picture.data, 1)
                            user.profile_picture = picture_file
                            user.password = generate_password_hash(
                                request.form.get("password"))
                            db.session.commit()
                            profile_picture = url_for(
                                'static', filename='images/profile_pics/' + user.profile_picture)
                            flash("Profile picture and password changed")
                            return redirect(url_for("user_profile", username=username))
                    elif request.form.get("emailaddress") != "" or request.form.get("emailaddress") != user.emailaddress:
                        # Changing picture and email
                        if request.form.get("password") == "":
                            picture_file = save_picture(form.picture.data, 1)
                            user.profile_picture = picture_file
                            # Checking email address is not already taken
                            emailaddress = request.form.get("emailaddress")
                            email_object = User.query.filter_by(
                                emailaddress=emailaddress).first()
                            if email_object:
                                flash("Email address is taken")
                                return redirect(url_for("user_profile", username=username))

                            user.emailaddress = request.form.get(
                                "emailaddress")
                            db.session.commit()
                            profile_picture = url_for(
                                'static', filename='images/profile_pics/' + user.profile_picture)
                            flash("Profile picture and email address changed")
                            return redirect(url_for("user_profile", username=username))
                        # When changing all three pieces of data
                        else:
                            picture_file = save_picture(form.picture.data, 1)
                            user.profile_picture = picture_file
                            # Checking email address is not already taken
                            emailaddress = request.form.get("emailaddress")
                            email_object = User.query.filter_by(
                                emailaddress=emailaddress).first()
                            if email_object:
                                flash("Email address is taken")
                                return redirect(url_for("user_profile", username=username))

                            user.emailaddress = request.form.get(
                                "emailaddress")
                            user.password = generate_password_hash(
                                request.form.get("password"))
                            db.session.commit()
                            profile_picture = url_for(
                                'static', filename='images/profile_pics/' + user.profile_picture)
                            flash(
                                "Profile picture, password and email address changed")
                            return redirect(url_for("user_profile", username=username))

            # Checking the 'New Password' field
            if request.form.get("password") != "":
                current = request.form.get("confirm_password")
                # This code checks that the password is correct
                if check_password_hash(user.password, current):
                    # Changing password only
                    if request.form.get("emailaddress") == "" or request.form.get("emailaddress") == user.emailaddress:
                        user.password = generate_password_hash(
                            request.form.get("password"))
                        db.session.commit()
                        flash("User password has been changed ")
                        return redirect(url_for("user_profile", username=username))
                    # Changing email and password
                    else:
                        # Checking email address is not already taken
                        emailaddress = request.form.get("emailaddress")
                        email_object = User.query.filter_by(
                            emailaddress=emailaddress).first()
                        if email_object:
                            flash("Email address is taken")
                            return redirect(url_for("user_profile", username=username))

                        user.emailaddress = request.form.get("emailaddress")
                        user.password = generate_password_hash(
                            request.form.get("password"))
                        db.session.commit()
                        flash("User password and email address have been changed ")
                        return redirect(url_for("user_profile", username=username))
                else:
                    # If password is incorrect
                    flash("Your current password is incorrect")

            # Changing email only
            elif request.form.get("password") == "" and request.form.get("emailaddress") != "" and request.form.get("emailaddress") != user.emailaddress:
                # Checking email address is not already taken
                emailaddress = request.form.get("emailaddress")
                email_object = User.query.filter_by(
                    emailaddress=emailaddress).first()
                if email_object:
                    flash("Email address is taken")
                    return redirect(url_for("user_profile", username=username))

                # We still need to run the code that checks the current password is correct
                current = request.form.get("confirm_password")
                if check_password_hash(user.password, current):
                    user.emailaddress = request.form.get("emailaddress")
                    db.session.commit()
                    flash("User email address has been changed")
                    return redirect(url_for("user_profile", username=username))
                else:
                    flash("Your current password is incorrect")

            # If no data is to be changed
            else:
                current = request.form.get("confirm_password")
                if check_password_hash(user.password, current):
                    flash("No user data was changed")
                    return redirect(url_for("user_profile", username=username))
                else:
                    flash("Your current password is incorrect")
    else:
        # if user is not logged in
        flash("You are not logged in.")
        return redirect(url_for("log_in"))
    title = "Edit User"
    return render_template("user_edit.html", user=user, team=team1, profile_picture=profile_picture, form=form, title=title)


# Delete User Function, returns user to log in page
# This function will cascade and delete the users team and players
@app.route("/delete_user/<username>")
def delete_user(username):
    # Log in check, to display correct navbar information
    if "user" in session:
        user = User.query.filter_by(username=username).first()
        if session["user"] == username:
            session.pop("user")
            # User deleted
            db.session.delete(user)
            db.session.commit()
            flash("Your account has been deleted")
            return redirect(url_for("log_in"))
        else:
            # If not the user
            flash("You cannot delete another managers account.")
            return redirect(url_for("user_profile", username=session["user"]))
    else:
        # If not logged in
        flash("You are not logged in.")
        return redirect(url_for("log_in"))


# Delete User Picture Function, returns user to profile page
@app.route("/delete_user_picture/<int:user_id>")
def delete_user_picture(user_id):
    if "user" in session:
        user = User.query.filter_by(id=user_id).first()
        if session["user"] == user.username:
            # Code to delete current image
            if user.profile_picture != 'default_manager.webp':
                os.remove(os.path.join(app.root_path,
                                       'static/images/profile_pics', user.profile_picture))
                user.profile_picture = 'default_manager.webp'
                db.session.commit()
                flash("Profile picture removed")
                return redirect(url_for("user_profile", username=session["user"]))
            else:
                # To stop the default images leaving repository
                flash("Cannot delete default picture")
                return redirect(url_for("user_profile", username=session["user"]))
        else:
            # If you are not user
            flash("Cannot remove another users picture.")
            return redirect(url_for("user_profile", username=session["user"]))
    else:
        # If you are not logged in
        flash("You are not logged in.")
        return redirect(url_for("log_in"))


# Delete squad picture function, returns user to team profile
@app.route("/delete_squad_picture/<int:team_id>")
def delete_squad_picture(team_id):
    # Log in check, to display correct navbar information
    if "user" in session:
        user = User.query.filter_by(username=session["user"]).first()
        team = Team.query.get_or_404(team_id)
        if user.id == team.users_id:
            # Code to delete current image
            if team.profile_picture != 'default_squad.webp':
                os.remove(os.path.join(app.root_path,
                                       'static/images/profile_pics', team.profile_picture))
                team.profile_picture = 'default_squad.webp'
                db.session.commit()
                flash("Squad picture removed")
                return redirect(url_for("team_profile", id=team.id))
            else:
                # To stop default images leaving repository
                flash("Cannot delete default picture")
                return redirect(url_for("team_profile", id=team.id))
        else:
            # If you are not user
            flash("Cannot remove another teams picture.")
            return redirect(url_for("user_profile", username=session["user"]))
    else:
        # If you are not logged in
        flash("You are not logged in")
        return redirect(url_for("log_in"))


# Live Scores API Page
@app.route("/live_scores", methods=["GET", "POST"])
def live_scores():
    # API Token to make the API accessible
    token = "75cf94657f2047ebbb9e09665358930d"
    headers = {
        'X-Auth-Token': token,
    }

    # Log in check, to display correct navbar information
    if "user" in session:
        user1 = User.query.filter_by(username=session["user"]).first()
        baseteam = Team.query.filter_by(team_name=user1.team_managed).first()
        profile_picture = url_for(
            'static', filename='images/profile_pics/' + user1.profile_picture)
    else:
        # If not logged in
        user1 = "None"
        baseteam = "None"
        profile_picture = "None"

    # Placing date given into needed format for the URL to function
    present = datetime.now()
    presentstring = present.strftime("%d/%m/%Y")
    data = requests.get(
        'https://api.football-data.org/v4/matches', headers=headers).json()
    if request.method == "POST":
        if request.form.get("match_date") == "":
            flash("Please select a date")
            return redirect(url_for("live_scores"))

        # Look at the date entered
        date_str = request.form.get("match_date")
        # Specify its format, ready to turn into a date from a string
        date_format = '%d/%m/%Y'
        # Turn into a date
        date_obj = datetime.strptime(date_str, date_format)
        # Now that it's a date, rearrange to how it's needed for the URL
        date = date_obj.strftime("%Y-%m-%d")
        data = requests.get(
            f'https://api.football-data.org/v4/matches/?date={date}', headers=headers).json()

        # Checking date is not in the future
        present = datetime.now()
        presentstring = present.strftime("%d/%m/%Y")
        if present.date() < date_obj.date():
            flash("Cannot select future date.")
            return redirect(url_for("live_scores"))

    matches = data['matches']
    title = "Live Scores"
    return render_template("live_scores.html", data=data, matches=matches, present=presentstring, user=user1, team=baseteam, profile_picture=profile_picture, title=title)
