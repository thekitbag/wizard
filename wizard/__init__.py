import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

app = Flask(__name__)
db = SQLAlchemy(app)
socketio = SocketIO(app)
app.config.from_object(os.environ['APP_SETTINGS'])

from wizard.models import User

import wizard.views
import wizard.messages
