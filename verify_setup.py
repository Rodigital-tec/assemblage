#!/usr/bin/env python3
"""
Script de vérification de la configuration de déploiement
"""

import os
import sys

def check_file(filename):
    """Vérifier si un fichier existe"""
    if os.path.exists(filename):
        print(f"✅ {filename}")
        return True
    else:
        print(f"❌ {filename} (MANQUANT)")
        return False

def check_directory(dirname):
    """Vérifier si un dossier existe"""
    if os.path.isdir(dirname):
        print(f"✅ {dirname}/")
        return True
    else:
        print(f"⚠️  {dirname}/ (optionnel)")
        return False

def main():
    print("=" * 60)
    print("🔍 Vérification de la configuration de déploiement")
    print("=" * 60)
    print()
    
    all_good = True
    
    # Vérifier les fichiers de configuration
    print("📋 Fichiers de configuration:")
    config_files = [
        'Procfile',
        'runtime.txt',
        'render.yaml',
        'requirements.txt',
        '.gitignore',
        '.env.example'
    ]
    
    for f in config_files:
        if not check_file(f):
            all_good = False
    
    print()
    
    # Vérifier les fichiers principaux
    print("📄 Fichiers principaux:")
    main_files = ['app.py', 'wsgi.py']
    
    for f in main_files:
        if not check_file(f):
            all_good = False
    
    print()
    
    # Vérifier les dossiers
    print("📁 Dossiers:")
    directories = ['static', 'routes']
    
    for d in directories:
        check_directory(d)
    
    print()
    
    # Vérifier les dépendances
    print("📦 Vérification des dépendances:")
    try:
        with open('requirements.txt', 'r') as f:
            content = f.read()
            if 'gunicorn' in content:
                print("✅ gunicorn trouvé")
            else:
                print("❌ gunicorn manquant")
                all_good = False
            
            if 'python-dotenv' in content:
                print("✅ python-dotenv trouvé")
            else:
                print("❌ python-dotenv manquant")
                all_good = False
    except Exception as e:
        print(f"❌ Erreur lors de la lecture de requirements.txt: {e}")
        all_good = False
    
    print()
    
    # Résumé
    print("=" * 60)
    if all_good:
        print("✅ Configuration OK ! Prêt pour le déploiement")
        print()
        print("Prochaines étapes:")
        print("1. git init")
        print("2. git add .")
        print("3. git commit -m 'Préparation déploiement'")
        print("4. Créer un dépôt GitHub")
        print("5. git push -u origin main")
        print("6. Déployer sur Render")
        return 0
    else:
        print("❌ Certains fichiers sont manquants")
        print("Veuillez vérifier la configuration")
        return 1

if __name__ == '__main__':
    sys.exit(main())

