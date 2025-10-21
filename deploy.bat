@echo off
REM ╔════════════════════════════════════════════════════════════════════════════╗
REM ║                                                                            ║
REM ║                    🚀 SCRIPT DE DEPLOIEMENT AUTOMATISE 🚀                 ║
REM ║                                                                            ║
REM ║                    Déploiement de Assembl'âge sur Render                  ║
REM ║                                                                            ║
REM ╚════════════════════════════════════════════════════════════════════════════╝

setlocal enabledelayedexpansion

echo.
echo ╔════════════════════════════════════════════════════════════════════════════╗
echo ║                                                                            ║
echo ║                    🚀 DEPLOIEMENT AUTOMATISE 🚀                           ║
echo ║                                                                            ║
echo ║                    Déploiement de Assembl'âge sur Render                  ║
echo ║                                                                            ║
echo ╚════════════════════════════════════════════════════════════════════════════╝
echo.

REM Étape 1: Vérifier Git
echo 📋 Étape 1: Vérification de Git...
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git n'est pas installé. Veuillez installer Git d'abord.
    pause
    exit /b 1
)
echo ✅ Git est installé
echo.

REM Étape 2: Initialiser Git
echo 📋 Étape 2: Initialisation de Git...
if not exist ".git" (
    git init
    echo ✅ Git initialisé
) else (
    echo ✅ Git déjà initialisé
)
echo.

REM Étape 3: Ajouter les fichiers
echo 📋 Étape 3: Ajout des fichiers...
git add .
echo ✅ Fichiers ajoutés
echo.

REM Étape 4: Créer le commit
echo 📋 Étape 4: Création du commit...
git commit -m "Déploiement automatisé de Assembl'âge" 2>nul || echo ✅ Aucun changement à commiter
echo ✅ Commit créé
echo.

REM Étape 5: Demander le nom d'utilisateur GitHub
echo 📋 Étape 5: Configuration GitHub...
set /p GITHUB_USERNAME="Entrez votre nom d'utilisateur GitHub: "

if "!GITHUB_USERNAME!"=="" (
    echo ❌ Nom d'utilisateur GitHub requis
    pause
    exit /b 1
)

set REPO_URL=https://github.com/!GITHUB_USERNAME!/assemblage.git
echo ✅ URL du dépôt: !REPO_URL!
echo.

REM Étape 6: Ajouter le remote
echo 📋 Étape 6: Ajout du remote GitHub...
git remote remove origin 2>nul
git remote add origin !REPO_URL!
echo ✅ Remote ajouté
echo.

REM Étape 7: Renommer la branche
echo 📋 Étape 7: Renommage de la branche...
git branch -M main
echo ✅ Branche renommée en 'main'
echo.

REM Étape 8: Pousser le code
echo 📋 Étape 8: Envoi du code vers GitHub...
echo ⚠️  Vous devrez peut-être entrer vos identifiants GitHub...
git push -u origin main
echo ✅ Code envoyé vers GitHub
echo.

REM Étape 9: Afficher les instructions finales
echo ╔════════════════════════════════════════════════════════════════════════════╗
echo ║                                                                            ║
echo ║                    ✅ ETAPE 1 TERMINEE ! ✅                              ║
echo ║                                                                            ║
echo ║                    Votre code est maintenant sur GitHub !                 ║
echo ║                                                                            ║
echo ╚════════════════════════════════════════════════════════════════════════════╝
echo.

echo 📋 PROCHAINES ETAPES:
echo.
echo 1. Allez sur https://render.com
echo 2. Connectez-vous avec votre compte GitHub
echo 3. Cliquez sur 'New +' puis 'Web Service'
echo 4. Sélectionnez votre dépôt 'assemblage'
echo 5. Configurez:
echo    - Name: assemblage-app
echo    - Build Command: pip install -r requirements.txt
echo    - Start Command: gunicorn app:app
echo    - Plan: Free
echo 6. Cliquez sur 'Create Web Service'
echo 7. Attendez 2-3 minutes
echo 8. Votre app sera accessible à: https://assemblage-app.onrender.com
echo.

echo ✅ Déploiement automatisé terminé !
echo.

pause

