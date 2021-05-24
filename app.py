from flask import Flask, jsonify, request, render_template
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
    if request.method == "POST":
        userInput = request.form.get("userInput")
        conversation.append(userInput)

        # Help function, type in help and you get help
        helpFunc = re.search(r"^.*help*.", userInput)
        if helpFunc:
            botResponse = "Hi here is some help"
            conversation.append(botResponse)
        
        #It's not done
        otherThing = re.search(r".*doing work", userInput)
        if otherThing:
            botResponse = "do your work"
            coversation.append(botResponse)

        return render_template('chat.html', conversation=conversation)
        print(conversation)
    return render_template('chat.html') # I'm sure this won't cause any problems later

app.run(debug=True)
