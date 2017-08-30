import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from config_reader import config_reader

# You may consider using a one-way hash to generate the password, and then
# use the hash again in the login view to perform the comparison. This is just
# for simplicity.
ADMIN_PASSWORD = config_reader('CONFIG')['admin_password']

# The secret key is used internally by Flask to encrypt session data stored
# in cookies. Make this unique for your app.
SECRET_KEY = config_reader('CONFIG')['secret_key']

APP_DIR = os.path.dirname(os.path.realpath(__file__))

# This is used by micawber, which will attempt to generate rich media
# embedded objects with maxwidth=800.
SITE_WIDTH = 800

# The playhouse.flask_utils.FlaskDB object accepts database URL configuration.
DEBUG = False

# Create a Flask WSGI app and configure it using values from the module.
app = Flask(__name__)
app.config.from_object(__name__)

#Postgres DB hookup
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/blog'
db = SQLAlchemy(app)
