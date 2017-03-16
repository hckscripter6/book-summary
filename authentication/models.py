from config import db, app
from flask_login import UserMixin


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(15), unique=True)
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(80))
	posts = db.relationship('Post', backref='user', lazy='dynamic')
	
	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password
	
	def __repr__(self):
		return '<User %r>' % (self.id)
		


							

