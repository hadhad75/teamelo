FROM python:3.7-alpine

# WORKDIR : permet de créer et de se placer dans un répertoire
# je place mon projet dans ce répertoire
WORKDIR /code

# permet de placer des variables au niveau de l'OS
# une variable d'environnement est accessible à toutes les applications
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

# RUN : permet d'exécuter une commande shell
RUN apk add --no-cache gcc musl-dev linux-headers

# COPY : permet de copier un fichier depuis l'OS hôte dans le conteneur
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# je copie le contenu du répertoire src dans le répertoire courant
# ici, nous plaçons le contenu dans le répertoire /code
COPY ./src .

# une fois que nous avons installé flask, 
# cela donne accès à une commande shell du même nom
# cette commande utilise la variable d'environne "FLASK_APP app.py" pour trouver le fichier
CMD ["flask", "run"]