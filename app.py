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

        # Help: type in help and you get help
        helpFunc = re.search(r"*.help*.", userInput)
        if helpFunc:
            botResponse = "Hi here is some help"
            conversation.append(botResponse)
        
        # Directions: Say I'm lost and then the bot will give instructions
        lost = re.search(r"^(im|i'm) lost*.|*.directions*.", userInput, re.IGNORECASE) # 
        if lost:
            lostConvo = []
            botResponse = ""
            conversation.append(botResponse)
            
        print(conversation)
        return render_template('chat.html', conversation=conversation)
    return render_template('chat.html') # I'm sure this won't cause any problems later

app.run(debug=True)
