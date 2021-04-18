#modulo inicial

from flask import Flask, render_template,request,redirect,url_for
# from flask_sqlalchemy import SQLAlchemy
# from flask_script import Manager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
# app.config['DEBUG'] = True
# SqlAlchemy Database Configuration With Mysql
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'senha-1234'

db = SQLAlchemy(app)

from controllers.default import *
from models import *
if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0',debug=True)

from models.tables import *


# migrate = Migrate(app, db)

# manager = Manager(app)
# manager.add_command('db', MigrateCommand)


# migrate = Migrate(app,db)
#
# manager = Manager(app)
# manager.add_command('db',MigrateCommand)
#

# from app.models import tables
# from app.controllers import default
