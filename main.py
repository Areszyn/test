from flask import Flask
from threading import Thread
from bot import main

app = Flask('')

@app.route('/')
def home():
    return "Bot is running"

def run():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    t = Thread(target=main)
    t.start()
    run()
