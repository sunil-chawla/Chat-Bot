from flask import Flask
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
english_bot = ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter")
@app.route("/")
def index():
     return "Hello World!"

if __name__ == "__main__":
     app.run(debug = True)
