import json
from flask import Blueprint, render_template, redirect, url_for, flash
from voterapp.models import Voter, Candidate, Constituency, Party
from voterapp import db
from flask_login import current_user, login_required

users = Blueprint('users', __name__)


@users.route('/vote', methods = ['GET', 'POST'])
@login_required
def vote():
    cid = current_user.cand_id
    if cid != None:
        flash('You have already Voted!')
        return redirect(url_for('home.dashboard'))
    con = Constituency.query.filter_by(const_code = current_user.const_code).first()
    candidates = con.candidates
    voter = current_user
    return render_template('users/vote.html', title = 'Vote', voter = voter, cand = candidates, con = con)


@users.route('/vote/<string:cand_id>', methods=['GET', 'POST'])
@login_required
def cast_vote(cand_id):
    candid = Candidate.query.filter_by(const_code = current_user.const_code).first().cand_id
    vs = Voter.query.filter_by(voter_id = current_user.voter_id).first().cand_id
    if(vs != None):
        flash('You have already voted!')
        return redirect(url_for('home.dashboard'))
    if(cand_id == 'CKAXXNO'):
        voter = Voter.query.filter_by(voter_id = current_user.voter_id).update(dict(cand_id = cand_id))
        db.session.commit()
        flash('Voting Successful!')
        return redirect(url_for('home.dashboard'))
    codelen = len(cand_id)
    if(codelen != 7):
        flash('Invalid ID!')
        return redirect(url_for('home.dashboard'))
    code = cand_id[0:5]
    if(code != candid[0:5]):
        flash('You cannot vote for this candidate!')
        return redirect(url_for('home.dashboard'))
    voter = Voter.query.filter_by(voter_id = current_user.voter_id).update(dict(cand_id = cand_id))
    db.session.commit()
    flash('Voting Successful!')
    return redirect(url_for('home.dashboard'))


@users.route('/vote/fetch/<string:party_no>',  methods=['GET', 'POST'])
def fetch_id(party_no):
    if(party_no == '8'):
        return json.dumps({'cand_id': 'CKAXXNO'});
    candidates = Candidate.query.filter_by(const_code = current_user.const_code, party_no = party_no).first()
    return json.dumps({'cand_id': candidates.cand_id});


@users.route('/results')
@login_required
def results():
    voter = current_user
    vs = Voter.query.filter_by(voter_id = current_user.voter_id).first().cand_id
    if(vs == None):
        flash('You have not voted yet. Please vote to see results.')
        return redirect(url_for('home.dashboard'))
    return render_template('users/results.html', title = 'Results', voter = voter)


@users.route('/candidates')
@login_required
def candidates():
    voter = current_user
    cand = Candidate.query.filter_by(const_code = current_user.const_code).all()
    party = Party.query.all()
    return render_template('users/candidates.html', title = 'Candidates', cand = cand, party = party, voter = voter)


@users.route('/account')
@login_required
def account():
    voter = current_user
    return render_template('users/account.html', title = 'Account', voter = voter)
