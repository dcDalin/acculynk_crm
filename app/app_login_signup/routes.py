from flask import Blueprint, render_template, request, url_for, redirect

mod = Blueprint('app_login_signup', __name__)

@mod.route('/login')
def login():
	page_title = 'Login Page'
	return render_template('app_login_signup/login.html', page_title=page_title)

@mod.route('/signup')
def signup():
	return render_template('app_login_signup/signup.html')