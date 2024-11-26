from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# Using HTML file, file must be in the same directory and named templates
@app.route("/<name>")
def home(name):
    return render_template("index.html", content=name, r=2, names=["Daniel", "David", "Bob"])

# # Unique route for user
# @app.route("/user/<name>")
# def user(name):
#     return f"Hello {name}"

# # If you have the ending slash, you can type the URL with or without it
# # But if you don't have it, the URL must not have the ending slash
# @app.route("/admin/")
# def admin():
#     # How to redirect with params
#   return redirect(url_for("user", name="Daniel"))

if __name__ == "__main__":
    app.run()
