from flask import Flask, request, render_template
import re

# List to keep track of what's been said
conversation = []

app = Flask(__name__)



# Homepage for the bot, provides user info on how to use it
@app.route('/')
def homepage():
    return render_template('index.html')

# The main bot function
@app.route('/bot', methods=["GET","POST"])
def bot():
    global conversation

    # Dictionary to store all keywords and responses
    responseDict = {
        ("hi", "hello"): "Hello! 👋",
        ("yo",): "sup",
        ("help",): "Help? Sure thing! I can help you with homework, study tips, ",
        
    }

    if request.method == "GET":
        if not conversation: # Check if the list is empty; if empty, send intro msg
            botMsg = "Hello, if you need help with anything, type 'help'"
            conversation.append(botMsg)
        return render_template('chat.html', conversation=conversation)

    if request.method == "POST":
        userInput = request.form.get("userInput") # Recieve user input from website
        conversation.append(userInput)
        userInput = userInput.lower()

        # TODO: Fix the key checking by using a pattern or something
        botMsg = "Sorry, I didn't understand that" # Default message 
        
        # Checking for keywords in the user input
        for key in responseDict:
            for keyword in key:
                if keyword in userInput:
                    botMsg = responseDict[key]
        conversation.append(botMsg)
        
        print(conversation)
        return render_template('chat.html', conversation=conversation)

app.run(debug=True)
