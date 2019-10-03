from flask import request, jsonify, render_template, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from sqlalchemy.orm import Query
from models import Login
import jsonpickle
import MySQLdb.cursors
import re

def login_route(app):
    login_url = "/login"
    db = SQLAlchemy()

    @app.route (login_url, methods=['GET'])
    def acti_page():
	    return render_template('login.html', titre="SignIn")

    @app.route(login_url, methods=['GET', 'POST'])
    def login():
         msg = ' '
        if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
            email = request.form['email']
            password=request.form['password']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM user WHERE email = %s AND password = %s', (email,password))
            user = cursor.fetchone()
            if user: 
                session['loggedin'] = True
                session['id'] = user['id']
                session['email'] = user['email']
                return "Connexion réussie ! Vous allez être redirigé vers la page d'accueil." # rediriger vers la page activité index
            else: 
                msg = 'email ou mot de passe incorrect'
        return render_template ('login.html', msg = msg)

    @app.route('/logout')
    def logout():
        session.pop('loggdin', None)
        session.pop('id', None)
        session.pop('email', None)
        return redirect(url_for('login'))

    @app.route('/loggedin/home')
    def home():
        if 'loggedin' in session:
            return render_template('index.html', email=session['email'])
        return redirect(url_for('login'))