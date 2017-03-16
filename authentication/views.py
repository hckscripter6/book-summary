from flask import Flask, render_template, redirect, request, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from authentication.forms import LoginForm, RegistrationForm
from authentication.models import User
from posts import views
from config import db, app


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
	
@app.route('/')
def index():
##	form = LoginForm()
#	if form.validate_on_submit():
#		return 'Form successfully submited'
	return render_template('index.html')
	
@app.route('/dashboard/login', methods=['POST', 'GET'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=request.form['email']).first()
		if user:
			if check_password_hash(user.password, request.form['password']):
				login_user(user)
				return redirect(url_for('dashboard'))
	return render_template('authentication/login.html', form=form)
	
'''@app.route('/dashboard/signup', methods=['GET', 'POST'])
def signup():
	form = RegistrationForm()
	if form.validate_on_submit():
		if request.form['password'] == request.form['confirm']:
			hashed_password = generate_password_hash(request.form['password'], method='sha256')
			new_user = User(username=request.form['username'], email=request.form['email'], password=hashed_password)
			db.session.add(new_user)
			db.session.commit()
			return '<h1>New user has been created!</h1>'	
	return render_template('authentication/signup.html', form=form)'''
	
	
@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))
	





