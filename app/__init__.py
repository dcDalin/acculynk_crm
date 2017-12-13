from flask import Flask

app = Flask(__name__)

from app.app_api.routes import mod
app.register_blueprint(app_api.routes.mod, url_prefix='/api')

from app.app_login_signup.routes import mod
app.register_blueprint(app_login_signup.routes.mod)

from app.app_static_pages.routes import mod
app.register_blueprint(app_static_pages.routes.mod)



