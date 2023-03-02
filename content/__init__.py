from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#from flask_login import LoginManager

app = Flask(__name__)       # creating instance of the class Flask

#region  --------------------- Create a security TOKEN  ---------------------------
app.config['SECRET_KEY'] = 'c2b69d65260d6d7fd2beec11b04bebc5'       # security token for the website, details below:
'''
this is to generate a random token:
Type 'python' on the Terminal  >>  type 'import secrets'  >>  type 'secrets.token_hex(16)'

'''
#endregion

#database = SQLAlchemy(app)

bcrypt = Bcrypt(app)

#login_manager = LoginManager(app)

from content import routes