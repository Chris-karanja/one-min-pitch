from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required
from . import main
from ..models import User
from .forms import UpdateProfile
from ..models import User, Pitch
from .. import db


@main.route('/')
def index():
    return render_template('index.html')
    pitches=Pitch.query.all()
    

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    if request.method == 'POST':
        new_pitch = Pitch(request.form['title'], request.form['text'])
        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('new.html')  