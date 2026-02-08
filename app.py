# medium-6-token-confusion/app.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG","CTF{dev}")

tokens = {}

@app.route("/")
def index():
    return """
<h2>Account Token Service</h2>
<ul>
<li>POST /token/issue</li>
<li>POST /reset</li>
<li>GET /health</li>
</ul>
"""

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

    if token in tokens:
        return jsonify({"status":"reset","flag":FLAG})

    return jsonify({"err":"bad"}),403

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
