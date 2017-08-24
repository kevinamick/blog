import os
from flask import Flask
from playhouse.flask_utils import FlaskDB

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
DATABASE = 'sqliteext:///%s' % os.path.join(APP_DIR, 'blog.db')
DEBUG = False

# Create a Flask WSGI app and configure it using values from the module.
app = Flask(__name__)
app.config.from_object(__name__)

# FlaskDB is a wrapper for a peewee database that sets up pre/post-request
# hooks for managing database connections.
flask_db = FlaskDB(app)

# The `database` is the actual peewee database, as opposed to flask_db which is
# the wrapper.
database = flask_db.database