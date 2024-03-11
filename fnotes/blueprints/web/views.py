from flask import render_template


def login():
    return render_template('login.html')

def notes():
    return render_template('notes.html')