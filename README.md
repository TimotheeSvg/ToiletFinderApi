# ToiletFinderApi

## Setup and run

Set les variable dans le .env pour de la prod ou du dev (prod utiliser le nom du service db en host, le port du service db non exposer)

> docker-compose up 

============

## Création / Update BDD (migration)

Se rendre dans le container:

> python manage.py migrate

===========


## Feed BDD

Se rendre dans le container

> python manage.py updateToilet

(fonction qui prends comme data tout les fichiers json du dossier /data, à vous de vérifier que celui-ci n'est pas vide)
