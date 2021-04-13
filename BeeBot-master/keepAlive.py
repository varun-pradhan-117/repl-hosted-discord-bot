'''
keepAlive runs a webserver on its own thread while the bot is running.
https://uptimerobot.com/ is used to ping the webserver every 10 minutes.
repl.it treats this ping as activity and prevents repl.it from shutting the program down
'''
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()