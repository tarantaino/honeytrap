from flask import Flask, jsonify, render_template
import sys
import os

#we allow python to check in the main directory so we can import database.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

app = Flask(__name__)

#this route loads the webpage

@app.route('/')
def index():
    return render_template("index.html")

#API that returns data in JSON format
@app.route('/api/attacks')
def api_attacks():
        attacks = get_all_attacks()
        return jsonify(attacks)

if __name__ == "__main__":
      print("Starting web server (Dashboard HoneyTrap) on port 5000...")
      app.run(debug = True, host = "0.0.0.0", port = 5000)