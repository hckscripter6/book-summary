from config import db
import datetime


#####Models######
	
class Post(db.Model):
	id = db.Column('id', db.Integer, primary_key=True)
	title = db.Column('title', db.String(90), unique=True)
	url = db.Column('url', db.String(90), unique=True)
	published = db.Column('published', db.DateTime())
	body = db.Column('body', db.Text(), unique=True)
	visibility = db.Column('visibility', db.String)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	
	def __init__(self, title, url, body, published, visibility, user_id):
		self.title = title
		self.url = url
		self.published = published
		self.body = body
		self.visibility = visibility
		self.user_id = user_id
	
		
	def __repr__(self):
		return '<Post %r>' % (self.title)
		
