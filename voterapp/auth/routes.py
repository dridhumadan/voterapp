from flask import Blueprint, render_template, redirect, url_for, flash
from voterapp import db
from voterapp.auth.forms import LoginForm, RegistrationForm
from voterapp.models import Voter
from flask_login import current_user, login_user, logout_user

auth = Blueprint('auth', __name__)


@auth.route('/auth/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        voter = Voter.query.filter_by(email_id = form.email_id.data).first()
        if voter is None or (voter.password != form.password.data):
            flash('Incorrect email or password')
            return redirect(url_for('auth.login'))
        login_user(voter, remember=True)
        return redirect(url_for('home.dashboard'))
    return render_template('auth/login.html', title = 'Login', form = form)


@auth.route('/auth/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        voter = Voter(voter_id = 'KA23001', email_id = form.email_id.data, password = form.password.data,
                      first_name = form.first_name.data, last_name = form.last_name.data, dob = form.dob.data, address = form.address.data,
                      const_code = form.constituency.data)
        db.session.add(voter)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form = form)


@auth.route('/auth/logout')
def logout():
    logout_user()
    return redirect(url_for('home.index'))