# 🚀 Déploiement Rapide - Assembl'âge sur Render

## ⚡ Résumé en 5 étapes

### 1️⃣ Initialiser Git
```bash
git init
git add .
git commit -m "Préparation déploiement Render"
```

### 2️⃣ Créer un dépôt GitHub
- Allez sur https://github.com/new
- Créez un dépôt `assemblage`
- Poussez votre code :
```bash
git remote add origin https://github.com/VOTRE_USERNAME/assemblage.git
git branch -M main
git push -u origin main
```

### 3️⃣ Créer un compte Render
- Allez sur https://render.com
- Cliquez "Sign up"
- Connectez votre compte GitHub

### 4️⃣ Déployer
- Dans Render, cliquez "New +" → "Web Service"
- Sélectionnez votre dépôt `assemblage`
- Remplissez :
  - **Name**: `assemblage-app`
  - **Build Command**: `pip install -r requirements.txt`
  - **Start Command**: `gunicorn app:app`
  - **Plan**: `Free`
- Cliquez "Create Web Service"

### 5️⃣ Configurer les variables
- Dans le dashboard Render, allez à "Environment"
- Ajoutez :
  ```
  FLASK_ENV=production
  SECRET_KEY=your_random_secret_key_here
  ```

## ✅ Fichiers prêts

- ✅ `Procfile` - Configuration serveur
- ✅ `runtime.txt` - Version Python
- ✅ `requirements.txt` - Dépendances (gunicorn + python-dotenv ajoutés)
- ✅ `render.yaml` - Configuration Render
- ✅ `.gitignore` - Fichiers à ignorer
- ✅ `.env.example` - Variables d'environnement

## 🎯 Résultat

Votre application sera accessible à :
```
https://assemblage-app.onrender.com
```

## 📝 Notes

- Plan gratuit : l'app s'arrête après 15 min d'inactivité
- SQLite n'est pas persistant (utilisez PostgreSQL pour la production)
- Déploiement automatique à chaque push sur GitHub

## 🆘 Besoin d'aide ?

Consultez `DEPLOIEMENT_RENDER.md` pour les détails complets.

---

**C'est tout ! Votre application est prête à être déployée ! 🎉**

