#!flask/bin/python
from app import app
from flask_socketio import SocketIO, emit
app.run(debug=True,host='0.0.0.0',threaded=True)
socketio.run(app, host='0.0.0.0')