# Utiliser une image Python officielle comme image de base
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires dans l'image Docker
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande par défaut pour lancer l'application
CMD ["python", "app.py"]
