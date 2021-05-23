from flask import Flask, jsonify, request, render_template
import re

app = Flask(__name__)

# Temporary homepage
@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/bot', methods=["GET","POST"])
def helpPage():
    if request.method == "POST":
        userInput = request.form.get("userInput")
        # Time for regex
        search = re.search(r"^help*.", userInput)
        if search:
            botResponse = "Hi here is some help"
            # Very finicky, need to fix
            return render_template('chat.html', botResponse=botResponse)
    return render_template('chat.html') # I'm sure this won't cause any problems later

app.run(debug=True)
