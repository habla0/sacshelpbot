from flask import Flask, jsonify, request, render_template
import re

app = Flask(__name__)

# Temporary homepage
@app.route('/')
def homepage():
    return render_template('index.html')

# Look, 
@app.route('/bot', methods=["GET","POST"])
def helpPage():
    if request.method == "POST":
        userInput = request.form.get("userInput")
        # Time for regex
        search = re.search(r"^help*.", userInput)
        if search:
            return "Hi here is some help"
    return render_template('chat.html')

app.run(debug=True)
