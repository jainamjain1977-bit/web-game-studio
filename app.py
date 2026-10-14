
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

items = ["rock", "paper", "scissor"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/play", methods=["POST"])
def play():
    data = request.get_json(silent=True) or {}
    user = data.get("choice", "").lower()

    if user not in items:
        return jsonify({"error": "Invalid choice"}), 400

    computer = random.choice(items)

    if user == computer:
        result = "Match Draw!"
        status = "draw"

    elif (
        (user == "rock" and computer == "scissor")
        or (user == "paper" and computer == "rock")
        or (user == "scissor" and computer == "paper")
    ):
        result = "🎉 You Win!"
        status = "win"

    else:
        result = "💻 Computer Wins!"
        status = "loss"

    return jsonify({
        "user": user,
        "computer": computer,
        "result": result,
        "status": status
    })


if __name__ == "__main__":
    app.run(debug=True)
