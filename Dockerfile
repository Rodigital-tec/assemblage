# Utiliser l'image Python officielle
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de requirements
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tous les fichiers de l'application
COPY . .

# Exposer le port 5000
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]

