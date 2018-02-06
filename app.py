from flask import Flask, render_template
import backend
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html", table = backend.retrieve_data())

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()