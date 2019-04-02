from flask import Blueprint, render_template, redirect, url_for
from voterapp.models import Voter, Candidate, Constituency
from voterapp import db
from flask_login import current_user, login_required

users = Blueprint('users', __name__)


@users.route('/vote', methods = ['GET', 'POST'])
@login_required
def vote():
    candidates = Candidate.query.filter_by(const_code = current_user.const_code).all()
    con = Constituency.query.filter_by(const_code = current_user.const_code).first().const_name
    return render_template('users/vote.html', title = 'Vote', cand = candidates, con = con)


@users.route('/vote/<string:cand_id>', methods=['GET', 'POST'])
def cast_vote(cand_id):
    voter = Voter.query.filter_by(voter_id = current_user.voter_id).update(dict(cand_id = cand_id))
    db.session.commit()
    return redirect(url_for('home.dashboard'))


@users.route('/candidates')
def candidates():
    return render_template('users/candidates.html', title = 'Candidates')
