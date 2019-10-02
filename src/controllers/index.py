from flask import request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Query
from models import Index
import jsonpickle

def index_route(app):
    index_url = "/index"
    db = SQLAlchemy()

    @app.route (index_url, methods=['GET'])
    def index_page():
	    return render_template('index.html', titre="page d'accueil")



