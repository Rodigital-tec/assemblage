#!/bin/bash

# ╔════════════════════════════════════════════════════════════════════════════╗
# ║                                                                            ║
# ║                    🚀 SCRIPT DE DEPLOIEMENT AUTOMATISE 🚀                 ║
# ║                                                                            ║
# ║                    Déploiement de Assembl'âge sur Render                  ║
# ║                                                                            ║
# ╚════════════════════════════════════════════════════════════════════════════╝

set -e

echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                            ║"
echo "║                    🚀 DEPLOIEMENT AUTOMATISE 🚀                           ║"
echo "║                                                                            ║"
echo "║                    Déploiement de Assembl'âge sur Render                  ║"
echo "║                                                                            ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo ""

# Étape 1: Vérifier Git
echo "📋 Étape 1: Vérification de Git..."
if ! command -v git &> /dev/null; then
    echo "❌ Git n'est pas installé. Veuillez installer Git d'abord."
    exit 1
fi
echo "✅ Git est installé"
echo ""

# Étape 2: Initialiser Git
echo "📋 Étape 2: Initialisation de Git..."
if [ ! -d ".git" ]; then
    git init
    echo "✅ Git initialisé"
else
    echo "✅ Git déjà initialisé"
fi
echo ""

# Étape 3: Ajouter les fichiers
echo "📋 Étape 3: Ajout des fichiers..."
git add .
echo "✅ Fichiers ajoutés"
echo ""

# Étape 4: Créer le commit
echo "📋 Étape 4: Création du commit..."
git commit -m "Déploiement automatisé de Assembl'âge" || echo "✅ Aucun changement à commiter"
echo "✅ Commit créé"
echo ""

# Étape 5: Demander le nom d'utilisateur GitHub
echo "📋 Étape 5: Configuration GitHub..."
read -p "Entrez votre nom d'utilisateur GitHub: " GITHUB_USERNAME

if [ -z "$GITHUB_USERNAME" ]; then
    echo "❌ Nom d'utilisateur GitHub requis"
    exit 1
fi

REPO_URL="https://github.com/$GITHUB_USERNAME/assemblage.git"
echo "✅ URL du dépôt: $REPO_URL"
echo ""

# Étape 6: Ajouter le remote
echo "📋 Étape 6: Ajout du remote GitHub..."
if git remote | grep -q origin; then
    git remote remove origin
fi
git remote add origin "$REPO_URL"
echo "✅ Remote ajouté"
echo ""

# Étape 7: Renommer la branche
echo "📋 Étape 7: Renommage de la branche..."
git branch -M main
echo "✅ Branche renommée en 'main'"
echo ""

# Étape 8: Pousser le code
echo "📋 Étape 8: Envoi du code vers GitHub..."
echo "⚠️  Vous devrez peut-être entrer vos identifiants GitHub..."
git push -u origin main
echo "✅ Code envoyé vers GitHub"
echo ""

# Étape 9: Afficher les instructions finales
echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                            ║"
echo "║                    ✅ ETAPE 1 TERMINEE ! ✅                              ║"
echo "║                                                                            ║"
echo "║                    Votre code est maintenant sur GitHub !                 ║"
echo "║                                                                            ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo ""

echo "📋 PROCHAINES ETAPES:"
echo ""
echo "1. Allez sur https://render.com"
echo "2. Connectez-vous avec votre compte GitHub"
echo "3. Cliquez sur 'New +' puis 'Web Service'"
echo "4. Sélectionnez votre dépôt 'assemblage'"
echo "5. Configurez:"
echo "   - Name: assemblage-app"
echo "   - Build Command: pip install -r requirements.txt"
echo "   - Start Command: gunicorn app:app"
echo "   - Plan: Free"
echo "6. Cliquez sur 'Create Web Service'"
echo "7. Attendez 2-3 minutes"
echo "8. Votre app sera accessible à: https://assemblage-app.onrender.com"
echo ""

echo "✅ Déploiement automatisé terminé !"
echo ""

