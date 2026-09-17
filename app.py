from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

balance = 10000

transactions = []


@app.route("/")
def home():
    return render_template(
        "index.html",
        balance=balance,
        transactions=transactions
    )


@app.route("/deposit", methods=["POST"])
def deposit():

    global balance

    amount = int(request.form["amount"])

    balance += amount

    transactions.append({
        "type": "Deposit",
        "amount": amount,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    return redirect("/")


@app.route("/withdraw", methods=["POST"])
def withdraw():

    global balance

    amount = int(request.form["amount"])

    if balance >= amount:

        balance -= amount

        transactions.append({
            "type": "Withdraw",
            "amount": amount,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7030)
