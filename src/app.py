from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_restful import
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
api = 
socketio = SocketIO(app)



if __name__ == '__main__':
    socketio.run(app)