from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, DateField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Length, EqualTo


class PostForm(FlaskForm):
	title = StringField('title', validators=[InputRequired()])
	url = StringField('url', validators=[InputRequired()])
	published = DateField('published', format='%m/%d/%Y', validators=[InputRequired()])
	visibility = RadioField('visibility', choices = [('private', 'private'), ('public', 'public')], default='private', validators=[InputRequired()] )
	body = TextAreaField('body', validators=[InputRequired()])
	
