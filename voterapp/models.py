from voterapp import db, login
from flask_login import UserMixin


@login.user_loader
def load_user(voter_id):
    return Voter.query.get(voter_id)


class Voter(UserMixin, db.Model):
    voter_id = db.Column(db.String(7), primary_key = True)
    email_id = db.Column(db.String(40), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(20), nullable = False)
    dob = db.Column(db.DateTime, nullable = False)
    address = db.Column(db.String(100), nullable = False)
    cand_id = db.Column(db.String(7))
    const_code = db.Column(db.String(4))

    def get_id(self):
        return (self.voter_id)


class Candidate(UserMixin, db.Model):
    cand_id = db.Column(db.String(7), primary_key = True)
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(20), nullable = False)
    party_no = db.Column(db.Integer)
    const_code = db.Column(db.String(4))


class Constituency(UserMixin, db.Model):
    const_code = db.Column(db.String(4), primary_key = True)
    const_name = db.Column(db.String(30), nullable = False)


class Party(UserMixin, db.Model):
    party_no = db.Column(db.Integer, primary_key = True)
    party_name = db.Column(db.String(30), nullable = False)
    address = db.Column(db.String(100), nullable = False)
