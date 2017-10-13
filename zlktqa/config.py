import os

SECRET_KEY = os.urandom(24)

# DEBUG    = True

HOST     = '127.0.0.1'
PORT     = '3306'
DATABASE = 'zlktqa'
USERNAME = 'root'
PASSWORD = 'Ppnn13mod'
DIALECT  = 'mysql'
DRIVER   = 'pymysql'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False