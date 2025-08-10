from flask import Flask, render_template, request, redirect, url_for
import csv, os
from datetime import datetime

app = Flask(__name__)

def save_message(name, email, message):
    fname = "messages.csv"
    header = not os.path.exists(fname)
    with open(fname, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(["Name","Email","Message","Timestamp"])
        writer.writerow([name, email, message, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name","").strip()
    email = request.form.get("email","").strip()
    message = request.form.get("message","").strip()
    if name and email and message:
        save_message(name, email, message)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
