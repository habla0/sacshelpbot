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

    # Dictionary to store all keywords and responses for conversation
    responseDict = {
        ("hi","hello"): "Hello! 👋",
        ("yo","hey"): "sup",
        ("help",): "Help? Sure thing! I can help you with homework/study tips and directions. What will it be?",
        ("work","study"): "Study it is! What subject/course do you want help with?",
        ("directions","lost"): "I can help with that. Are you in the BBC or SAH (cathedral counts as SAH)?", # Fun fact: user's location is never used
        ("maths","mathematics"): "Go to Wolfram Alpha to solve your problems! Seriously it's really useful.",
        ("software","computer science","compsci","sdd"): "Go to Stack Overflow to solve your problems! It's pretty good.",
        ("science","chemistry","physics","biology"): "Good luck lol. Revise all of your notes.",
        ("earth and environmental science","ees","ess"): "not real subjects 😐",
        ("bbc","sah"): "Okay, now what room do you want to go to?",
        ("sweet", "thank"): "You're welcome!",
        ("i hate you","you suck","cringe"): "😭😭 my feelings :((",
        ("time management",): "Hey author here: really not in a postion to teach time management sorry",
        ("how are you",): "I'm not bad, I guess.",
        ("english",): "Start preparing early! Quote tables and drafts are your best friend (other than me of course) :)",
        ("ib",): "Sorry, I don't speak cringe.",
        ("hsc",): "Infinitely better than the IB I feel."
        # I really can't think of more things to add rn - 2:31am, 1/06/2021
    }

    if request.method == "GET":
        if not conversation: # Check if the list is empty; if empty, send intro msg
            botMsg = "Hello, if you need help with anything, type 'help'. I'd be able to chat with you if the author wasn't so lazy"
            conversation.append(botMsg)
        return render_template('chat.html', conversation=conversation)

    if request.method == "POST":
        userInput = request.form.get("userInput") # Recieve user input from website
        conversation.append(userInput)
        userInput = userInput.lower() # make it all lowercase so case doesn't matter

        botMsg = "Sorry, I didn't understand that." # Default message 
        
        # Checking for keywords in the user input
        for key in responseDict:
            for keyword in key:
                print(keyword)
                if keyword in userInput:
                    print("USER INPUT IS:",userInput)
                    print('RESPONSE:',keyword)
                    botMsg = responseDict[key]

        # Check if room is valid
        bbcRoom = re.search(r"^B(LG|G|1|2|3|4)..", conversation[-1], re.IGNORECASE)
        sahRoom = re.search(r"^S(4|5|6|7|8|9)..", conversation[-1], re.IGNORECASE)
        destinationRoom = conversation[-1] # The room the user has stated to be their destination

        # If the room is in the BBC
        if bbcRoom:
            if destinationRoom[1] == 'l':
                botMsg = "Head to the ground floor of the BBC and head down the stairs."
            elif destinationRoom[1] == 'g':
                botMsg = "Head to the ground floor of the BBC."
            elif destinationRoom[1] == '1':
                botMsg = "Head to the BBC and go to level 1."
            elif destinationRoom[1] == '2':
                botMsg = "Head to the BBC and go to level 2."
            elif destinationRoom[1] == '3':
                botMsg = "Head to the BBC and go to level 3."
            elif destinationRoom[1] == '4':
                botMsg = "Head to the BBC and go to level 4."

        # If the room is in the SAH
        elif sahRoom:
            if destinationRoom[1] == '4':
                botMsg = "Head to the SAH, take the lift or stairs to level 4."
            elif destinationRoom[1] == '5':
                botMsg = "Head to the SAH, take the lift or stairs to level 5."
            elif destinationRoom[1] == '6':
                botMsg = "Head to the SAH, take the lift or stairs to level 6."
            elif destinationRoom[1] == '7':
                botMsg = "Head to the SAH, take the lift or stairs to level 7."
            elif destinationRoom[1] == '8':
                botMsg = "Head to the SAH, take the lift or stairs to level 8."
            elif destinationRoom[1] == '9':
                botMsg = "Head to the SAH, take the lift or stairs to level 8 and then go up to the roof."
        
        # If room doesn't exist
        else:
            print("INVALID ROOM DINGUS")

        conversation.append(botMsg)

        return render_template('chat.html', conversation=conversation)

app.run(debug=True)
