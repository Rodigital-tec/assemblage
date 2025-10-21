# Guide de Déploiement - Assembl'âge sur Render

## Étapes de déploiement

### 1. Préparer votre code pour Git

```bash
# Initialiser un dépôt Git (si ce n'est pas déjà fait)
git init
git add .
git commit -m "Préparation pour déploiement sur Render"
```

### 2. Créer un compte Render

1. Allez sur https://render.com
2. Cliquez sur "Sign up"
3. Créez un compte avec votre email

### 3. Connecter votre dépôt Git

1. Connectez votre compte GitHub/GitLab à Render
2. Autorisez Render à accéder à vos dépôts

### 4. Créer un nouveau service Web

1. Dans le dashboard Render, cliquez sur "New +"
2. Sélectionnez "Web Service"
3. Connectez votre dépôt
4. Remplissez les informations :
   - **Name**: `assemblage-app`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: `Free` (pour tester)

### 5. Configurer les variables d'environnement

Dans les paramètres du service, allez à "Environment" et ajoutez :

```
FLASK_ENV=production
SECRET_KEY=your_random_secret_key_here
```

### 6. Déployer

1. Cliquez sur "Create Web Service"
2. Render va automatiquement déployer votre application
3. Attendez que le déploiement soit terminé (environ 2-3 minutes)

### 7. Accéder à votre application

Une fois déployée, vous recevrez une URL comme :
```
https://assemblage-app.onrender.com
```

## Dépannage

### L'application ne démarre pas
- Vérifiez les logs dans le dashboard Render
- Assurez-vous que tous les fichiers sont présents
- Vérifiez que `requirements.txt` contient toutes les dépendances

### Erreur de base de données
- Render utilise SQLite par défaut
- Les données seront perdues lors du redéploiement
- Pour la production, utilisez PostgreSQL (gratuit sur Render)

### Comment ajouter PostgreSQL

1. Dans Render, créez une nouvelle base de données PostgreSQL
2. Copiez l'URL de connexion
3. Ajoutez-la comme variable d'environnement `DATABASE_URL`

## Notes importantes

- **Plan gratuit**: L'application s'arrête après 15 minutes d'inactivité
- **Données**: SQLite n'est pas persistant sur Render, utilisez PostgreSQL pour la production
- **Limites**: 0.5 GB de RAM, 0.5 CPU

## Prochaines étapes

Pour une meilleure expérience :
1. Migrez vers PostgreSQL
2. Configurez un domaine personnalisé
3. Mettez en place des sauvegardes automatiques
4. Configurez les logs et monitoring

