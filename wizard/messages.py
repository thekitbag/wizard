from wizard import socketio
from flask import request

@socketio.on('connect')
def handle_connection():
	sid = request.sid
	print("player connected")
	print(sid) 