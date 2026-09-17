from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

accounts = {
    "100001": {"name": "Sampath", "balance": 5000},
    "100002": {"name": "Rakesh", "balance": 10000},
    "100003": {"name": "Karthik", "balance": 7000}
}

transactions = []


@app.route("/")
def home():

    search = request.args.get("search", "").lower()

    filtered_accounts = {}

    for acc_no, details in accounts.items():

        if (
            search == ""
            or search in acc_no.lower()
            or search in details["name"].lower()
        ):
            filtered_accounts[acc_no] = details

    return render_template(
        "index.html",
        accounts=filtered_accounts,
        transactions=transactions
    )


@app.route("/deposit", methods=["POST"])
def deposit():

    account_no = request.form["account_no"]
    amount = int(request.form["amount"])

    accounts[account_no]["balance"] += amount

    transactions.append({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "account": account_no,
        "customer": accounts[account_no]["name"],
        "type": "Deposit",
        "amount": amount,
        "balance": accounts[account_no]["balance"]
    })

    return redirect("/")


@app.route("/withdraw", methods=["POST"])
def withdraw():

    account_no = request.form["account_no"]
    amount = int(request.form["amount"])

    if amount <= accounts[account_no]["balance"]:

        accounts[account_no]["balance"] -= amount

        transactions.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "account": account_no,
            "customer": accounts[account_no]["name"],
            "type": "Withdraw",
            "amount": amount,
            "balance": accounts[account_no]["balance"]
        })

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7030)
