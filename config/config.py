import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
        'these-are-not-the-droids-you-are-looking-for'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql://user:password@localhost/db_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    data_url = 'http://49.12.237.145:5150/'