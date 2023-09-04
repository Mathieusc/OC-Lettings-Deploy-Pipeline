![Orange County Lettings banner](https://user.oc-static.com/upload/2023/07/20/1689880374259_Orange%20County%20Lettings%20Ad.png)  
## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Déploiement

Le déploiement sur Heroku nécessite les critères suivants:

- Un compte CircleCI
- Un compte Docker Hub
- Un compte Heroku
- Un compte Sentry

Créer un fichier .env en local avec les valeurs suivantes:
- `SECRET_KEY`='Clé_secrète_Django'
- `DEBUG`='Valeur' (0 = False, 1 = True)
- `ALLOWED_HOSTS`='['localhost', 'nom_application']
- `SENTRY_DSN`='Clé_Sentry'

Pour la pipeline de CircleCI:

- Avoir un compte CircleCI
- Autoriser le projet
- Dans les options du projet, renseigner les variables d'environnements suivantes:
  - `DOCKER_PWD`: Mot de passe Docker Hub
  - `DOCKER_USER`: Nom de compte Docker Hub
  - `HEROKU_APP`: Nom de l'application
  - `HEROKU_TOKEN`: Jeton d'authentification pour Heroku
  
Remplacer dans le fichier `.circleci/config.yml`
`mathieusc/oc-lettings` par `votre-dépôt-Docker-Hub`

Lors d'un push sur la branche main uniquement, le déploiement Heroku sera automatiquement effectué depuis l'image Docker.  
Les tests et le linting seront vérifiés (avec pytest et flake8) avant le déploiement.
