from flask import Blueprint, render_template, request, url_for, redirect

mod = Blueprint('app_static_pages', __name__)

@mod.route('/')
@mod.route('/index')
def index():
	return render_template('app_static_pages/index.html')

@mod.route('/about')
def about():
	return render_template('app_static_pages/about.html')

@mod.route('/contact')
def contact():
	return render_template('app_static_pages/contact.html')