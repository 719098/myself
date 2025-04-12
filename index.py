from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("myself.html")
@app.route("/holland")
def holland():
    return render_template("holland.html")
@app.route("/career")
def career():
    return render_template("career.html")


if __name__ == "__main__":
    app.run(debug=True)
