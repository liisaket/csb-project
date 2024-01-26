import os
from flask import abort, request, session

# for Flaw 3: Broken authentication: fix by importing the appropriate library
# from werkzeug.security import check_password_hash, generate_password_hash

from sqlalchemy.sql import text
from db import db

def login(username,password):
    # Flaw 1: SQL injection: poor SQL query that allows attackers perfom an injection attack.
    # Attacker can login by entering the following: ' or ''='
    sql = text("SELECT * FROM users WHERE username='"+username+"' AND passwd='"+password+"'")
    # Fix by correcting the query:
    # sql = text("SELECT passwd, id FROM users WHERE username=:username")
    
    result = db.session.execute(sql, {"username":username,"password":password})
    user = result.fetchone()

    # Flaw 2: Security misconfiguration: does not verify the received password is correct.
    # Fix by checking the user's password against received password. Use hashed passwords.
    # if user and check_password_hash(user[2], password):
    if user:
        session["user_id"] = user[1]
        session["username"] = username
        session["csrf_token"] = os.urandom(16).hex()
        return True
    return False

def logout():
    del session["user_id"]
    del session["username"]
    del session["csrf_token"]

def register(name, password):
    # Flaw 3: Broken authentication: uses plain text passwords
    # Fix by using hash values:
    # hash_value = generate_password_hash(password)

    try: 
        sql = text("INSERT INTO users (username,passwd) VALUES (:username,:passwd)")
        # db.session.execute(sql, {"username":name,"password":hash_value})
        db.session.execute(sql, {"username":name,"passwd":password})
        db.session.commit()
        return True
    except:
        return False

def check_username(username):
    if len(username) < 1 or len(username) > 20:
        return False
    return True

def check_password(password1):
    if password1 == "":
        return False
    return True

def check_passwords(password1, password2):
    if password1 != password2:
        return False
    return True

def user_id():
    return session.get("user_id")

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)