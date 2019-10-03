from flask import request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Query
#from models import Index
import jsonpickle

def index_route(app):
    index_url = "/index"
    login_url = "/login"
    act_url = "/act/zumba"
    mass_url = "/massage"
    actsp_url = "/activitessportives"
    actbe_url = "/activitesbienetre"
    voyages_url = "/voyages"
    maldives_url = "/maldives"

    db = SQLAlchemy()

    @app.route (index_url, methods=['GET'])
    def index_page():
	    return render_template('index.html', titre="page d'accueil")

    @app.route (login_url, methods=['GET'])
    def connexion_page():
        return render_template('login.html', titre='SignIn')
    
    @app.route (act_url, methods=['GET'])
    def activite():
        return render_template('activite1.html', titre='Zumba')
    
    @app.route (mass_url, methods=['GET'])
    def massage_page():
        return render_template('massage.html', titre='Massage')
    
    @app.route (actsp_url, methods=['GET'])
    def activite_sportives():
        return render_template('activitessportives.html', titre='Activités Sportives')
    
    @app.route (actbe_url, methods=['GET'])
    def activite_bienetre():
        return render_template('activitesbienetre.html', titre='Activités Bien-Être')

    @app.route (voyages_url, methods=['GET'])
    def voyages():
        return render_template('voyages.html', titre='Voyages')
    
    @app.route (maldives_url, methods=['GET'])
    def maldives():
        return render_template('maldives.html', titre='Voyage aux Maldives')