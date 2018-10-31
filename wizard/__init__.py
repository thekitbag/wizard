import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

app = Flask(__name__)
db = SQLAlchemy()
socketio = SocketIO(app)

app.config.from_object(os.environ['APP_SETTINGS'])

db.init_app(app)
app.secret_key = "development-key"

import wizard.views
import wizard.messages

print(os.environ['APP_SETTINGS'])