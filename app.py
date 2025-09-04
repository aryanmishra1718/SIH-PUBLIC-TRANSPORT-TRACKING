from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return "<h2>About Page</h2><p>This project helps track buses in real-time for small cities.</p>"

@app.route("/contact")
def contact():
    return "<h2>Contact Page</h2><p>Contact us at: team@sihproject.com</p>"

if __name__ == "__main__":
    app.run(debug=True)