import random

from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "secret_key"  # セッションを使うために必要


@app.route("/", methods=["GET", "POST"])
def index():
    if "secret_number" not in session:
        session["secret_number"] = random.randint(1, 100)
        session["attempts"] = 0
        session["message"] = ""

    if request.method == "POST":
        guess = int(request.form["guess"])
        session["attempts"] += 1

        if guess == session["secret_number"]:
            session["message"] = (
                f'正解！ {session["secret_number"]} が正解でした。 {session["attempts"]}回で当てました。'
            )
            session.pop("secret_number", None)  # ゲームクリア時に秘密の数字を削除
        elif guess < session["secret_number"]:
            session["message"] = "もっと大きい数です。"
        else:
            session["message"] = "もっと小さい数です。"

    return render_template("index.html", message=session["message"], attempts=session["attempts"])


if __name__ == "__main__":
    app.run(debug=True)
