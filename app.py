from flask import Flask, jsonify, request, render_template
import requests
import re

app = Flask(__name__)

# Temporary homepage
@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/bot')
def botpage():
    userInput = request.args["userInput"]
    return render_template('chat.html')

app.run(debug=True)
