import os
import sys

# Ajouter le répertoire courant au path
sys.path.insert(0, os.path.dirname(__file__))

# Importer l'app depuis app.py
from app import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

