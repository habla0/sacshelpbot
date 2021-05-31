from flask import Flask, request, render_template
import re

conversation = []

app = Flask(__name__)

# Temporary homepage
@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/bot', methods=["GET","POST"])
def bot():
    global conversation

    responseDict = {
        "help": "Help msg",
        "homework": "do homework",
        "where": "ahhhh",
        "another": "beep"
    }

    if request.method == "GET":
        return render_template('chat.html', conversation=conversation)

    if request.method == "POST":
        userInput = request.form.get("userInput")
        conversation.append(userInput)

        botMsg = "default"
        for key in responseDict:
            if key in userInput:
                botMsg = responseDict[key]
        conversation.append(botMsg)
        
        print(conversation)
        return render_template('chat.html', conversation=conversation)
    #return render_template('chat.html') # I'm sure this won't cause any problems later

app.run(debug=True)
