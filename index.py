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
@app.route("/future")
def future():
    return render_template("future_work.html")
@app.route("/about")
def about():
    return render_template("aboutme.html")
@app.route("/skills")
def skills():
    return render_template("skills.html")




if __name__ == "__main__":
    app.run(debug=True)
