# -*- coding: utf-8 -*-
from flask import Flask, redirect, render_template, request, url_for, session
from app import app
from user_db import User
import hashlib

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        password = hashlib.sha512(password).hexdigest()

        user = User().check_user(name, password)

        if user:
            return "Login success"

            session['user'] = user
        else:
            return "User not exist"

        # return "Login success"

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if password != password2:
            return "Password not match"

        password = hashlib.sha512(password).hexdigest()

        User().register(name, password)

        return "Success"






            




