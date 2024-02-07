from flask import render_template, request, redirect, session
from app import app
import users
import notes

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/error")
def error():
    return render_template("error.html", message="you are not logged in")

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    # Flaw 5: Broken access control: attacker can act as a user without being logged in.
    # Fix flaw 5 by checking if a user is logged in.
    
    # if users.user_id():
      if request.method == "GET":
        all_notes = notes.get_notes()
        return render_template("welcome.html", all_notes=all_notes)
      if request.method == "POST":
          # For flaw 3 / flaw 5 fix also:
          # users.check_csrf()
          note = request.form["note"]
          notes.add_note(note)
      return redirect("welcome")

    # If line 19 fails:
    # return redirect("/error")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not users.login(username, password):
            return render_template("login.html", message="wrong username or password")
        return redirect("welcome")

@app.route("/logout")
def logout():
    if users.user_id():
        users.logout()
        return redirect("/")
    return render_template("error.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        if not users.check_username(username):
            return render_template("register.html", message="error: username must be 1-20 characters")

        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if not users.check_passwords(password1, password2):
            return render_template("register.html", message="error: passwords differ")
        if not users.check_password(password1):
            return render_template("register.html", message="error: please enter a password")

        if not users.register(username, password1):
            return render_template("register.html", message="error: registration failed")
        return render_template("register.html", message="registration was successful")
