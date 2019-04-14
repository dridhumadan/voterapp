from flask import Blueprint, render_template, redirect, url_for, flash
from voterapp.models import Voter, Candidate, Constituency, Party
from voterapp import db
from flask_login import current_user, login_required

users = Blueprint('users', __name__)


@users.route('/vote', methods = ['GET', 'POST'])
@login_required
def vote():
    cid = Voter.query.filter_by(voter_id = current_user.voter_id).first().cand_id
    if cid != None:
        return render_template('users/vote_complete.html', title = 'Vote')
    candidates = Candidate.query.filter_by(const_code = current_user.const_code).all()
    con = Constituency.query.filter_by(const_code = current_user.const_code).first().const_name
    return render_template('users/vote.html', title = 'Vote', cand = candidates, con = con, login_status = 2)


@users.route('/vote/<string:cand_id>', methods=['GET', 'POST'])
@login_required
def cast_vote(cand_id):
    voter = Voter.query.filter_by(voter_id = current_user.voter_id).update(dict(cand_id = cand_id))
    db.session.commit()
    flash('Voting Successful!')
    return redirect(url_for('home.dashboard'))

@users.route('/results')
@login_required
def results():
    return render_template('users/results.html', title = 'Results')


@users.route('/candidates')
@login_required
def candidates():
    cand = Candidate.query.filter_by(const_code = current_user.const_code).all()
    party = Party.query.all()
    return render_template('users/candidates.html', title = 'Candidates', cand = cand, party = party)


@users.route('/account')
@login_required
def account():
    return render_template('users/account.html', title = 'Account')
