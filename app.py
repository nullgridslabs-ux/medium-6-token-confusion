# medium-6-token-confusion/app.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG","CTF{dev}")

tokens = {}

@app.route("/health")
def health():
    return "ok"

@app.route("/token/issue", methods=["POST"])
def issue():
    user = request.json["user"]
    t = f"T-{user}"
    tokens[t] = user
    return jsonify({"token":t})

@app.route("/reset", methods=["POST"])
def reset():
    token = request.json["token"]

    # BUG: same token accepted for any purpose
    if token in tokens:
        return jsonify({"status":"reset","flag":FLAG})

    return jsonify({"err":"bad"}),403

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
