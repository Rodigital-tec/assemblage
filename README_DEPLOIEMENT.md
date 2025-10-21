# 🚀 Déploiement Assembl'âge sur Render

## 📌 Vue d'ensemble

Votre application **Assembl'âge** est maintenant prête à être déployée sur **Render**, un serveur de test gratuit et fiable.

```
┌─────────────────────────────────────────────────────────────┐
│                    VOTRE APPLICATION                        │
│                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐ │
│  │   Frontend   │    │   Backend    │    │  Database    │ │
│  │   (HTML/CSS) │───▶│   (Flask)    │───▶│  (SQLite)    │ │
│  └──────────────┘    └──────────────┘    └──────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ Déployer sur
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                      RENDER (Gratuit)                       │
│                                                             │
│  https://assemblage-app.onrender.com                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## ✅ Fichiers créés

| Fichier | Description |
|---------|-------------|
| `Procfile` | Configuration du serveur web |
| `runtime.txt` | Version Python (3.11.7) |
| `render.yaml` | Configuration Render |
| `requirements.txt` | Dépendances (gunicorn + python-dotenv ajoutés) |
| `.gitignore` | Fichiers à ignorer dans Git |
| `.env.example` | Variables d'environnement |

## 🎯 Étapes rapides

### 1. Initialiser Git
```bash
git init
git add .
git commit -m "Préparation déploiement"
```

### 2. Créer un dépôt GitHub
- Allez sur https://github.com/new
- Créez un dépôt `assemblage`
- Poussez votre code

### 3. Déployer sur Render
- Allez sur https://render.com
- Connectez votre GitHub
- Créez un "Web Service"
- Sélectionnez votre dépôt

### 4. Configurer les variables
- `FLASK_ENV=production`
- `SECRET_KEY=your_secret_key`

### 5. Attendre le déploiement
- 2-3 minutes
- Votre app sera accessible à : `https://assemblage-app.onrender.com`

## 📚 Documentation

| Document | Contenu |
|----------|---------|
| `QUICK_START.md` | Guide rapide (5 étapes) |
| `DEPLOIEMENT_RENDER.md` | Guide complet avec détails |
| `COMMANDES_GIT.txt` | Commandes Git prêtes à copier-coller |
| `CHECKLIST_DEPLOIEMENT.md` | Checklist complète |
| `RESUME_DEPLOIEMENT.txt` | Résumé complet |

## 🔧 Modifications effectuées

### app.py
- ✅ Support des variables d'environnement
- ✅ Configuration automatique pour production
- ✅ Support de PostgreSQL (optionnel)

### requirements.txt
- ✅ Ajout de `gunicorn` (serveur web)
- ✅ Ajout de `python-dotenv` (gestion des variables)

## ⚠️ Limitations du plan gratuit

| Limitation | Détail |
|-----------|--------|
| ⏱️ Inactivité | L'app s'arrête après 15 min d'inactivité |
| 💾 Stockage | 0.5 GB de RAM |
| 🔧 CPU | 0.5 CPU |
| 📊 Base de données | SQLite n'est pas persistant |

## 💡 Recommandations

### Pour tester
- ✅ Utilisez le plan gratuit avec SQLite
- ✅ Testez les fonctionnalités principales
- ✅ Vérifiez les logs pour les erreurs

### Pour la production
- 🔄 Utilisez PostgreSQL pour la persistance
- 🔐 Configurez un domaine personnalisé
- 📊 Mettez en place des sauvegardes
- 📈 Configurez le monitoring

## 🚀 Commencer

1. **Lisez** `QUICK_START.md` pour un guide rapide
2. **Suivez** les étapes ci-dessus
3. **Consultez** `DEPLOIEMENT_RENDER.md` pour les détails
4. **Utilisez** `COMMANDES_GIT.txt` pour les commandes

## 🆘 Besoin d'aide ?

- 📖 Consultez les fichiers de documentation
- 🔗 Visitez https://render.com/docs
- 💬 Contactez le support Render

## 🎉 Résultat

Votre application sera accessible à :
```
https://assemblage-app.onrender.com
```

---

**Votre application est prête ! Commencez maintenant ! 🚀**

