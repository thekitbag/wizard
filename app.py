from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO
from models import db, User




app = Flask(__name__)
socketio = SocketIO(app)





  
if __name__ == "__main__":  
  socketio.run(app, host='0.0.0.0', debug=True)

