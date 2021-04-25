from flask import Flask, jsonify
import re

app = Flask(__name__)

@app.route('/')
def homepage():
    return '<h1 style="font-family: Comic Sans MS", sans-serif>0 bobux</h1>'

app.run(debug=True)
