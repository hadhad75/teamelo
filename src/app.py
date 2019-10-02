import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# dans le répertoire controllers il y a un fichier annonce
from controllers import index
#import de la fonction envoi d'email
#from flask_mail import Mail
# on récupère les variables d'environnement (variables au niveau de l'OS)
DB_STRING = os.environ['DB_STRING']
SRV_PORT = os.environ['SRV_PORT']

# chargement de Flask
app = Flask("Projet", template_folder='views', static_folder='static')


# chargement de l'ORM alchemy
app.config['SQLALCHEMY_DATABASE_URI'] = DB_STRING
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

#demarrage des routes
index.index_route(app)

#serveur SMTP
# mail_settings = {
#     "MAIL_SERVER": 'smtp.gmail.com',
#     "MAIL_PORT": 465,
#     "MAIL_USE_TLS": False,
#     "MAIL_USE_SSL": True,
#     "MAIL_USERNAME": os.environ['bonappart937@gmail.com'],
#     "MAIL_PASSWORD": os.environ['ajcloud*']
# }

# app.config.update(mail_settings)
# mail = Mail(app)



# démarrage du serveur
app.run(host='0.0.0.0', port=SRV_PORT)