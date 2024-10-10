from flask import Blueprint, flash, render_template, jsonify, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from backend.Forms.auth import LoginForm, RegistrationForm
from backend.models.models import db, User

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('auth.dashboard'))
    return render_template('reg.html', form=form)

@auth_blueprint.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return jsonify({"message": f"Hello, {current_user.username}. Welcome to your dashboard!"})

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Make sure you have a login form
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('auth.dashboard'))
        else:
            flash('Login failed. Check your email and password.', 'danger')
    return render_template('login.html', form=form)

@auth_blueprint.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "You have been logged out."})