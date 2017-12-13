from flask import Blueprint

mod = Blueprint('app_api', __name__)

@mod.route('/users')
def users():
	return '{"name": "Dalin Oluoch", "email": "mcdalinoluoch@gmail.com"}'
	