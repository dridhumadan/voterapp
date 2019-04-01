from flask import Blueprint, render_template

users = Blueprint('users', __name__)


@users.route('/vote', methods = ['GET', 'POST'])
def vote():
    return render_template('users/vote.html', title = 'Vote')


@users.route('/candidates')
def candidates():
    return render_template('users/candidates.html', title = 'Candidates')
