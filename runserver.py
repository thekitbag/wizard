from wizard import app
from wizard import socketio

if __name__ == "__main__":
	socketio.run(app, host='0.0.0.0', debug=True)

