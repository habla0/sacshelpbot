from flask import Flask, jsonify, request
from flask_socketio import SocketIO
import re
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return '<h1 style="font-family: Comic Sans MS", sans-serif>0 bobux</h1>'

@app.route('/bot')
def bot():
    

app.run(debug=True)
