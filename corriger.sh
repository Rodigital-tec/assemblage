#!/bin/bash

# ╔════════════════════════════════════════════════════════════════════════════╗
# ║                                                                            ║
# ║                    🔧 CORRECTION AUTOMATIQUE 🔧                           ║
# ║                                                                            ║
# ║                    Erreur GitHub: "failed to push some refs"              ║
# ║                                                                            ║
# ╚════════════════════════════════════════════════════════════════════════════╝

clear

echo ""
echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                            ║"
echo "║                    🔧 CORRECTION AUTOMATIQUE 🔧                           ║"
echo "║                                                                            ║"
echo "║                    Erreur GitHub: 'failed to push some refs'              ║"
echo "║                                                                            ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo ""
echo ""

# Étape 1: Vérifier Git
echo "📋 Étape 1/3: Vérification de Git..."
if ! command -v git &> /dev/null; then
    echo "❌ Git n'est pas installé."
    exit 1
fi
echo "✅ Git est installé"
echo ""

# Étape 2: Télécharger les fichiers du dépôt
echo "📋 Étape 2/3: Téléchargement des fichiers du dépôt GitHub..."
git pull origin main --allow-unrelated-histories
if [ $? -ne 0 ]; then
    echo "⚠️  Erreur lors du téléchargement"
    echo "   Essayez de résoudre les conflits manuellement"
    exit 1
fi
echo "✅ Fichiers téléchargés"
echo ""

# Étape 3: Envoyer le code
echo "📋 Étape 3/3: Envoi du code vers GitHub..."
git push -u origin main
if [ $? -ne 0 ]; then
    echo "❌ Erreur lors de l'envoi"
    echo "   Vérifiez que:"
    echo "   1. Votre dépôt GitHub existe et est PUBLIC"
    echo "   2. Vous avez accès à Internet"
    echo "   3. Vos identifiants GitHub sont corrects"
    exit 1
fi
echo "✅ Code envoyé vers GitHub"
echo ""

# Afficher le succès
clear

echo ""
echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                            ║"
echo "║                    ✅ ERREUR CORRIGEE ! ✅                               ║"
echo "║                                                                            ║"
echo "║                    Votre code est maintenant sur GitHub !                 ║"
echo "║                                                                            ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo ""
echo ""

echo "📋 PROCHAINES ETAPES:"
echo ""
echo "1. Allez sur: https://render.com"
echo "2. Connectez-vous avec GitHub"
echo "3. Cliquez sur 'New +' puis 'Web Service'"
echo "4. Sélectionnez votre dépôt 'assemblage'"
echo "5. Configurez et déployez"
echo ""

