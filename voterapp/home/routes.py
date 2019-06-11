from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from voterapp.models import Constituency, Voter, Candidate, Party

home = Blueprint('home', __name__)


@home.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('home.dashboard'))
    return render_template('home/index.html')


@home.route('/dashboard')
@login_required
def dashboard():
    voter = current_user
    constituency = Constituency.query.filter_by(const_code = current_user.const_code).first()
    noc = len(constituency.candidates) + 1
    return render_template('home/dashboard.html', title = 'Dashboard', voter = voter, cname = constituency.const_name, noc = noc)


@home.route('/admin')
@login_required
def admin():
    if (current_user.email_id != 'admin@voterapp.com'):
        return render_template('errors/401.html') , 401
    voters = Voter.query.all()
    parties = Party.query.all()
    candidates = Candidate.query.all()
    constituencies = Constituency.query.all()
    return render_template('home/admin.html', title = 'Admin Page', voters = voters , parties = parties, candidates = candidates, constituencies = constituencies)
    