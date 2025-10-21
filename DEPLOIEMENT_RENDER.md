# 🚀 Déploiement de Assembl'âge sur Render

## ✅ Fichiers de déploiement créés

Votre application est maintenant prête pour le déploiement ! Les fichiers suivants ont été créés :

- ✅ **Procfile** - Configuration pour Render
- ✅ **runtime.txt** - Version Python (3.11.7)
- ✅ **render.yaml** - Configuration Render avancée
- ✅ **.gitignore** - Fichiers à ignorer dans Git
- ✅ **.env.example** - Variables d'environnement
- ✅ **requirements.txt** - Dépendances mises à jour (ajout de gunicorn et python-dotenv)

## 📋 Étapes de déploiement

### Étape 1 : Initialiser Git

```bash
git init
git add .
git commit -m "Préparation pour déploiement sur Render"
```

### Étape 2 : Créer un compte Render

1. Allez sur **https://render.com**
2. Cliquez sur **"Sign up"**
3. Créez un compte avec votre email

### Étape 3 : Connecter votre dépôt

1. Allez sur **https://github.com** (ou GitLab)
2. Créez un nouveau dépôt public
3. Poussez votre code :

```bash
git remote add origin https://github.com/votre-username/assemblage.git
git branch -M main
git push -u origin main
```

### Étape 4 : Déployer sur Render

1. Connectez-vous à **https://render.com**
2. Cliquez sur **"New +"** → **"Web Service"**
3. Sélectionnez votre dépôt GitHub
4. Remplissez les informations :
   - **Name**: `assemblage-app`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: `Free`

### Étape 5 : Configurer les variables d'environnement

Dans le dashboard Render, allez à **"Environment"** et ajoutez :

```
FLASK_ENV=production
SECRET_KEY=your_random_secret_key_here
```

### Étape 6 : Déployer

1. Cliquez sur **"Create Web Service"**
2. Attendez le déploiement (2-3 minutes)
3. Votre application sera accessible à : `https://assemblage-app.onrender.com`

## 🔧 Configuration modifiée

### app.py
- Ajout du support des variables d'environnement
- Configuration automatique pour production
- Support de PostgreSQL (optionnel)

### requirements.txt
- Ajout de `gunicorn` (serveur web)
- Ajout de `python-dotenv` (gestion des variables d'environnement)

## ⚠️ Limitations du plan gratuit

- ⏱️ L'application s'arrête après 15 minutes d'inactivité
- 💾 SQLite n'est pas persistant (données perdues au redéploiement)
- 🔧 0.5 GB de RAM, 0.5 CPU

## 💡 Recommandations

### Pour la production :
1. **Utilisez PostgreSQL** au lieu de SQLite
2. **Configurez un domaine personnalisé**
3. **Mettez en place des sauvegardes**
4. **Activez les logs et monitoring**

### Pour ajouter PostgreSQL :
1. Créez une base de données PostgreSQL sur Render (gratuit)
2. Copiez l'URL de connexion
3. Ajoutez-la comme variable `DATABASE_URL`

## 🆘 Dépannage

### L'application ne démarre pas
- Vérifiez les logs dans le dashboard Render
- Assurez-vous que `requirements.txt` est complet
- Vérifiez que `app.py` est à la racine

### Erreur 502 Bad Gateway
- Attendez quelques minutes (déploiement en cours)
- Vérifiez les logs pour les erreurs

### Base de données vide
- C'est normal avec SQLite sur Render
- Utilisez PostgreSQL pour la persistance

## 📞 Support

- Documentation Render : https://render.com/docs
- Documentation Flask : https://flask.palletsprojects.com
- Support Render : https://render.com/support

---

**Votre application est prête ! 🎉**

Commencez par l'étape 1 et suivez les instructions ci-dessus.

