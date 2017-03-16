from flask import Flask, render_template, redirect, request, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from config import db, app
from posts.models import Post
from authentication.models import User
from posts.forms import PostForm

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#loop through posts
@app.route('/')
def read():
	post = Post.query.filter_by(visibility='public').order_by(Post.published.desc()).all()
	return render_template('index.html', post=post)

	
#select individual post
@app.route('/post/<post_url>')
def select(post_url):
	post = Post.query.filter_by(visibility='public').order_by(Post.published.desc()).all()
	single = Post.query.filter_by(url=post_url).first_or_404()
	return render_template('posts/select.html', post=post, single=single)

	
#create posts
@app.route('/dashboard/create', methods=['POST', 'GET'])
@login_required
def create():
	admin = True
	form = PostForm()
	the_id = current_user.get_id()
	if form.validate_on_submit():
		if request.method == 'POST':
			post = Post(request.form['title'], request.form['url'], request.form['body'], request.form['published'], request.form['visibility'], the_id)
			db.session.add(post)
			db.session.commit()
			return redirect(url_for('dashboard'))
	return render_template('posts/create.html', form=form, admin=admin)

	
#delete posts
@app.route('/dashboard/post/<int:post_id>/delete-this-post_pw{GreenHillZone91}', methods=['POST', 'GET'])
@login_required
def delete(post_id):
	post = Post.query.filter_by(id=post_id).first()
	db.session.delete(post)
	db.session.commit()
	return redirect(url_for('read'))
	
	
#edit posts
@app.route('/post/<post_url>/edit', methods=['POST', 'GET'])
@login_required
def update(post_url):
	admin = True
	post = Post.query.filter_by(url=post_url).first_or_404()
	form = PostForm(request.form)
	form.title.data = post.title
	form.url.data = post.url  	
	form.published.data = post.published  
	form.visibility.data = post.visibility  
	form.body.data = post.body  
	if request.method == 'POST':
		post.title = request.form['title']
		post.url = request.form['url']
		post.body = request.form['body']
		post.published = request.form['published']
		post.visibility = request.form['visibility']
		db.session.commit()
		return redirect(url_for('read'))
	return render_template('posts/update.html', form=form, admin=admin)
	
	
@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
	admin = True
	public = Post.query.filter_by(visibility='public').order_by(Post.published.desc()).all()
	private = Post.query.filter_by(visibility='private').order_by(Post.published.desc()).all()
	return render_template('/dashboard.html', public=public, private=private, admin=admin)
	
