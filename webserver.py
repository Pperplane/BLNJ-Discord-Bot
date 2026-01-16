from flask import Flask
from threading import Thread

# datetime for the terminal to print out time for reference if there's slow down or used for references
from datetime import datetime

# Formatting date time for easy usage
def datetimeStr():
    datetimeFormat = "%Y-%m-%d %H:%M:%S"
    datetimeNow = datetime.now().strftime(datetimeFormat)
    datetimestr = f"[{datetimeNow}]"
    return datetimestr

app = Flask('')
@app.route('/')
def home():
    return f"{datetimeStr()}: 🟢 Bot Web Server is Running"

def run():
    """
    Runs the Web Server
    """
    app.run(host="0.0.0.0", port="8080")

def keep_alive():
    t = Thread(target=run)
    t.start()

