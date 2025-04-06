# Tournoi de Football ⚽

Application web de gestion de tournoi de football, développée en Python avec Django et Django REST Framework.

---

## 📅 Fonctionnalités

- Création d'équipes avec nom et ville
- Ajout de joueurs à une équipe avec limite de 11
- Organisation de matchs entre deux équipes
- Attribution automatique de points :
  - 3 pts pour victoire
  - 1 pt pour match nul
  - 0 pt pour défaite
- Calcul dynamique du classement selon les règles
- Interface API REST (DRF) + formulaire HTML pour ajouter un joueur
- Limitation automatique à 11 joueurs par équipe

---

## 🪖 Stack technique

- Python 3.9+
- Django 4.x
- Django REST Framework
- SQLite (par défaut)
- Bootstrap 5 (formulaire HTML)

---

## ⚡ Installation

### 1. Cloner le repo
```bash
git clone https://github.com/votre-utilisateur/tournoi-football.git
cd tournoi-football
```

### 2. Créer et activer un environnement virtuel
```bash
python3.9 -m venv env
source env/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Lancer les migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Démarrer le serveur
```bash
python manage.py runserver
```

---

## 🔗 Endpoints API REST principaux

| Fonction | URL |
|---------|-----|
| Liste/création des équipes | `/api/equipes/` |
| Liste/création des joueurs | `/api/joueurs/` |
| Liste/création des matchs  | `/api/matchs/`  |
| Classement dynamique | `/api/classement/` |
| Formulaire HTML (ajout joueur) | `/api/joueur/new/` |

---

## 🌟 Bonus possibles

- [x] Dockerisation de l’application
- [x] Interface frontend enrichie avec Bootstrap
- [ ] Intégration Vue ou React (non faite)
- [ ] Intégration Elasticsearch pour recherche avancée

---

## 📊 Tests

Lancer les tests unitaires :
```bash
python manage.py test football
```

---

## 🚀 Déploiement (Docker)

### 1. Fichier `Dockerfile`
```Dockerfile
# Dockerfile
FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### 2. Fichier `docker-compose.yml`
```yaml
version: '3.9'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/code
    command: python manage.py runserver 0.0.0.0:8000
```

### 3. Démarrage avec Docker :
```bash
docker-compose up --build
```

---
