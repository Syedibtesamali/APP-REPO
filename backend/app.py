
from flask import Flask, jsonify, send_from_directory
import random
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_FOLDER = os.path.join(BASE_DIR, "../frontend")

@app.route("/")
def home():
    return send_from_directory(FRONTEND_FOLDER, "index.html")

@app.route("/<path:filename>")
def frontend_files(filename):
    return send_from_directory(FRONTEND_FOLDER, filename)

@app.route("/guess")
def guess():
    number = random.randint(1, 10)
    return jsonify({
        "message": "Random number generated",
        "number": number
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

