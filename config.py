from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

#####Configuration#####

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123qweasdzxc!@#@localhost/sandbox'
Bootstrap(app)
db = SQLAlchemy(app)




app.config['SECRET_KEY'] = 'J8$lsK3#sJs73J'
app.config['SECURITY_REGISTERABLE'] = True
