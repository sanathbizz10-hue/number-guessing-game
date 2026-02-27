from flask import Flask, render_template_string, request
import random
import os

app = Flask(__name__)

number = random.randint(1, 100)
attempts = 0

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Number Guessing Game</title>
</head>
<body style="text-align:center; font-family:Arial; margin-top:50px;">
    <h1>🎮 Number Guessing Game</h1>
    <p>Guess a number between 1 and 100</p>
    <form method="POST">
        <input type="number" name="guess" required>
        <button type="submit">Guess</button>
    </form>
    <p>{{ message }}</p>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    global number, attempts
    message = ""

    if request.method == "POST":
        guess = int(request.form["guess"])
        attempts += 1

        if guess == number:
            message = f"🎉 Correct! You guessed it in {attempts} attempts!"
            number = random.randint(1, 100)
            attempts = 0
        elif guess < number:
            message = "Too low!"
        else:
            message = "Too high!"

    return render_template_string(html, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
