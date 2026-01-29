# Utilise une image Python légère et récente
FROM python:3.11-slim

# Définit le répertoire de travail dans le container
WORKDIR /app

# Copie d'abord requirements.txt pour profiter du cache Docker (plus rapide aux rebuilds)
COPY requirements.txt .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie tout le reste du projet
COPY . .

# Expose le port 5000 (celui de Flask)
EXPOSE 5000

# Commande pour lancer l'application
CMD ["python", "view.py"]
