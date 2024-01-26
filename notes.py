from db import db
from sqlalchemy.sql import text

def get_notes():
    sql = text("SELECT note, id FROM notes")
    result = db.session.execute(sql)
    return result.fetchall()

def add_note(note):
    sql = text("INSERT INTO notes (note) VALUES (:note) RETURNING id")
    result = db.session.execute(sql, {"note":note})
    db.session.commit()
    return result.fetchone()[0]