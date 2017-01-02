import os

#grab the folder where this script
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'

WTF_CSRF_ENABLED = True
SECRET_KEY = 'myprecious'

#define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

#tell SQLAlchemy where to access to database
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ DATABASE_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = True
