from flask import request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Query
from models import Activite
import jsonpickle

def activite_route(app):
    act_url = "/act/zumba"
    db = SQLAlchemy()

    @app.route (act_url, methods=['GET'])
    def acti_page():
	    return render_template('activite1.html', titre="Cours de Zumba")

    @app.route(act_url, methods=['POST'])
    def create():
         restaurant = {
             'name': test
         }
         return jsonify(restaurant), 200
