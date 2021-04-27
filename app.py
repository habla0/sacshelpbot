from flask import Flask, jsonify, send_file
import re

app = Flask(__name__)

@app.route('/')
def homepage():
    return '<h1 style="font-family:Comic Sans MS;text-align:center;font-size:100px;">go to /drip or you have 0 bobux</h1>'

@app.route('/drip')
def spicy():
    return send_file("test_image.jpg") # I need to find a way to get this working with HTML

app.run(debug=True)
