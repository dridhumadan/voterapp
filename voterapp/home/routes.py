from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from voterapp.models import Constituency

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
    const_name = Constituency.query.filter_by(const_code = current_user.const_code).first().const_name
    return render_template('home/dashboard.html', title = 'Dashboard', login_status = 1, voter = voter, cname = const_name)
