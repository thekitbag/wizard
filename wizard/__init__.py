from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

app = Flask(__name__)
db = SQLAlchemy()
socketio = SocketIO(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/wizard'
db.init_app(app)
app.secret_key = "development-key"

import wizard.views
import wizard.messages