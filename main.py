from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/expertise")
def expertise():
    return render_template("expertise.html")

if __name__ == "__main__":
    app.run()