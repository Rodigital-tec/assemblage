# ✅ Checklist de Déploiement - Assembl'âge

## 📋 Avant de commencer

- [ ] Vous avez un compte GitHub (https://github.com)
- [ ] Vous avez un compte Render (https://render.com)
- [ ] Git est installé sur votre ordinateur
- [ ] Vous avez accès à ce dossier

## 🔧 Configuration locale

- [ ] Fichier `Procfile` existe
- [ ] Fichier `runtime.txt` existe
- [ ] Fichier `requirements.txt` contient `gunicorn` et `python-dotenv`
- [ ] Fichier `.gitignore` existe
- [ ] Fichier `app.py` est à la racine
- [ ] Dossier `static/` existe
- [ ] Dossier `routes/` existe

## 📝 Initialisation Git

- [ ] Exécutez : `git init`
- [ ] Exécutez : `git add .`
- [ ] Exécutez : `git commit -m "Préparation déploiement Render"`
- [ ] Vérifiez : `git log --oneline` (vous devez voir votre commit)

## 🌐 Créer un dépôt GitHub

- [ ] Allez sur https://github.com/new
- [ ] Créez un dépôt nommé `assemblage`
- [ ] Sélectionnez "Public"
- [ ] Cliquez "Create repository"
- [ ] Copiez l'URL du dépôt

## 📤 Pousser le code sur GitHub

- [ ] Exécutez : `git remote add origin https://github.com/VOTRE_USERNAME/assemblage.git`
- [ ] Exécutez : `git branch -M main`
- [ ] Exécutez : `git push -u origin main`
- [ ] Vérifiez sur GitHub que votre code est présent

## 🚀 Déployer sur Render

- [ ] Allez sur https://render.com
- [ ] Connectez-vous avec GitHub
- [ ] Cliquez "New +" → "Web Service"
- [ ] Sélectionnez votre dépôt `assemblage`
- [ ] Remplissez les informations :
  - [ ] Name: `assemblage-app`
  - [ ] Environment: `Python 3`
  - [ ] Build Command: `pip install -r requirements.txt`
  - [ ] Start Command: `gunicorn app:app`
  - [ ] Plan: `Free`
- [ ] Cliquez "Create Web Service"

## 🔐 Configurer les variables d'environnement

- [ ] Dans le dashboard Render, allez à "Environment"
- [ ] Ajoutez la variable `FLASK_ENV` avec la valeur `production`
- [ ] Ajoutez la variable `SECRET_KEY` avec une clé aléatoire
- [ ] Cliquez "Save"

## ⏳ Attendre le déploiement

- [ ] Attendez 2-3 minutes
- [ ] Vérifiez les logs pour les erreurs
- [ ] Votre application devrait être accessible à : `https://assemblage-app.onrender.com`

## 🧪 Tester l'application

- [ ] Ouvrez l'URL de votre application
- [ ] Vérifiez que la page d'accueil se charge
- [ ] Testez la connexion (admin@assemblage.ch / admin123)
- [ ] Testez quelques fonctionnalités

## 📊 Monitoring

- [ ] Vérifiez les logs dans le dashboard Render
- [ ] Vérifiez que l'application ne s'arrête pas
- [ ] Vérifiez que les erreurs sont minimes

## 🎉 Succès !

- [ ] Votre application est en ligne !
- [ ] Vous pouvez partager l'URL avec d'autres
- [ ] Vous pouvez continuer à développer et pousser des mises à jour

## 📝 Notes supplémentaires

### Pour les mises à jour futures

```bash
# Après chaque modification
git add .
git commit -m "Description de vos modifications"
git push origin main
# Render redéploiera automatiquement !
```

### Pour ajouter PostgreSQL (optionnel)

- [ ] Créez une base de données PostgreSQL sur Render
- [ ] Copiez l'URL de connexion
- [ ] Ajoutez-la comme variable `DATABASE_URL` dans Render
- [ ] Redéployez

### Pour configurer un domaine personnalisé (optionnel)

- [ ] Achetez un domaine (GoDaddy, Namecheap, etc.)
- [ ] Dans Render, allez à "Custom Domain"
- [ ] Suivez les instructions pour configurer le DNS

## 🆘 Dépannage

### L'application ne démarre pas
- [ ] Vérifiez les logs dans Render
- [ ] Vérifiez que `requirements.txt` est complet
- [ ] Vérifiez que `app.py` est à la racine

### Erreur 502 Bad Gateway
- [ ] Attendez quelques minutes
- [ ] Vérifiez les logs
- [ ] Redéployez si nécessaire

### Base de données vide
- [ ] C'est normal avec SQLite
- [ ] Utilisez PostgreSQL pour la persistance

---

**Félicitations ! Votre application est déployée ! 🎉**

Pour plus d'informations, consultez :
- `QUICK_START.md` - Guide rapide
- `DEPLOIEMENT_RENDER.md` - Guide complet
- `COMMANDES_GIT.txt` - Commandes Git

