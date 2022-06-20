from flask import Flask, render_template, request, redirect, session
# import the class from user.py
from flask_app.models.user import User

from flask_app import app

@app.route('/users')
def index():
    users = User.get_all()
    return render_template("index.html", all_users = users)

@app.route('/users/new')
def new_user():
    return render_template("users.html")

@app.route('/users/<int:num>')
def user_page(num):
    user = User.get_info(num)
    return render_template("user_page.html", this_user = user)

@app.route('/users/<int:num>/edit')
def user_edit(num):
    user = User.get_info(num)
    return render_template("user_edit.html", this_user = user)

@app.route('/users/<int:num>/delete')
def delete_user(num):
    User.delete(num)
    return redirect('/users')

@app.route('/users/new/process', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')

@app.route('/users/update/process/<int:num>', methods=["POST"])
def update_user(num):
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "id": num,
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.edit(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')