from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    