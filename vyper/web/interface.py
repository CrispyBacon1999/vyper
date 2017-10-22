from flask import Flask, render_template
import threading
app = Flask(__name__)
bot_name = "Vyper-Bot"


def run(url, name="Vyper-bot"):
    bot_name = name
    thread = threading.Thread(target=app.run, args=[url])
    thread.daemon = True
    thread.start()