from flask import Flask
from threading import Thread

# This web server exists to keep bot running full-time

app = Flask('')

@app.route('/')
def home():
  return "Running..."

def run():
  app.run(host='0.0.0.0', port=8080)

def keepAlive():
  t = Thread(target=run)
  t.start()