from flask import Flask, jsonify, request, render_template
import requests
import re

app = Flask(__name__)

# Temporary homepage
@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/bot', methods=["GET","POST"])
def botpage():
    if request.method == "POST":
        userInput = request.form.get("userInput")
        print(userInput)
    return render_template('chat.html')

app.run(debug=True)
