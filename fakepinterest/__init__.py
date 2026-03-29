from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
app.config["SECRET_KEY"] = "9be6138e203011db9aafdb365704351b"
app.config['UPLOAD_FOLDER'] = 'static/fotos_posts'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_vier = 'homepage'

from fakepinterest import routes
