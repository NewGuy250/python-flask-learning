from flask import Flask, redirect, url_for
# Initialize App
app = Flask(__name__)
# Define path
@app.route("/")
def home():
    # Return text also HTML
    return "Hello World! <h1>Oof</h1>"
# Using the <> tags means whatever is in the path can be used as a variable
@app.route("/<name>")
def user(name):
    return f"Hello {name}"
# Redirects users
@app.route("/admin")
def admin():
    # url_for takes the function name
    return redirect(url_for("home"))

# Run webpage
if __name__ == "__main__":
    app.run()