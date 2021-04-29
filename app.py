from flask import Flask, jsonify, send_file
from flask_socketio import SocketIO
import re

app = Flask(__name__)

@app.route('/')
def homepage():
    return '<h1 style="font-family: Comic Sans MS", sans-serif>0 bobux go to /drip</h1>'

@app.route('/drip')
def spicy():
    return send_file("test_image.jpg")



app.run(debug=True)
