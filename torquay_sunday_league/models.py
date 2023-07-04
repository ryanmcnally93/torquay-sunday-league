from torquay_sunday_league import db


class Team(db.Model):
    #schema for the Team model
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(25), unique=True, nullable=False)
    team_no_of_players = db.Column(db.Integer, primary_key=False, nullable=False)
    team_colour = db.Column(db.String(30), nullable=False)
    team_location = db.Column(db.String(25), unique=True, nullable=False)
    players = db.relationship(
        "Player", backref="team", cascade="all, delete", lazy=True)

    def __repr__(self):
        #__repr__ to represent itself in the form of a string
        return self



class Player(db.Model):
    #schema for the Player model
    id = db.Column(db.Integer, primary_key=True)
    player_kit_number = db.Column(
        db.Integer, unique=True, primary_key=False, nullable=False)
    player_name = db.Column(db.String(20), unique=True, nullable=False)
    player_position = db.Column(db.String(15), nullable=False)
    player_joined = db.Column(db.Date, nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey(
        "team.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        #__repr__ to represent itself in the form of a string
        return "#{0} - Kit Number: {1} | Name: {2} | Joined: {4}".format(
            self.id, self.player_kit_number, self.player_name, self.player_joined
        )


class User(db.Model):
    """ User Model """

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    emailaddress = db.Column(db.String(35), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

