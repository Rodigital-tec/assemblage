@echo off
REM ╔════════════════════════════════════════════════════════════════════════════╗
REM ║                                                                            ║
REM ║                    🚀 DEPLOIEMENT COMPLET AUTOMATISE 🚀                   ║
REM ║                                                                            ║
REM ║                    Assembl'âge sur Render                                 ║
REM ║                                                                            ║
REM ║                    UNE SEULE COMMANDE = TOUT EST FAIT !                  ║
REM ║                                                                            ║
REM ╚════════════════════════════════════════════════════════════════════════════╝

setlocal enabledelayedexpansion

cls
echo.
echo ╔════════════════════════════════════════════════════════════════════════════╗
echo ║                                                                            ║
echo ║                    🚀 DEPLOIEMENT COMPLET AUTOMATISE 🚀                   ║
echo ║                                                                            ║
echo ║                    Assembl'âge sur Render                                 ║
echo ║                                                                            ║
echo ║                    UNE SEULE COMMANDE = TOUT EST FAIT !                  ║
echo ║                                                                            ║
echo ╚════════════════════════════════════════════════════════════════════════════╝
echo.
echo.

REM Étape 1: Vérifier Git
echo 📋 Étape 1/5: Vérification de Git...
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git n'est pas installé. Veuillez installer Git d'abord.
    echo    Téléchargez Git ici: https://git-scm.com/download/win
    pause
    exit /b 1
)
echo ✅ Git est installé
echo.

REM Étape 2: Initialiser Git
echo 📋 Étape 2/5: Initialisation de Git...
if not exist ".git" (
    git init
    echo ✅ Git initialisé
) else (
    echo ✅ Git déjà initialisé
)
echo.

REM Étape 3: Ajouter les fichiers
echo 📋 Étape 3/5: Ajout des fichiers...
git add .
echo ✅ Fichiers ajoutés
echo.

REM Étape 4: Créer le commit
echo 📋 Étape 4/5: Création du commit...
git commit -m "Déploiement automatisé de Assembl'âge" 2>nul || echo ✅ Aucun changement à commiter
echo ✅ Commit créé
echo.

REM Étape 5: Demander le nom d'utilisateur GitHub
echo 📋 Étape 5/5: Configuration GitHub...
echo.
echo ⚠️  IMPORTANT: Vous devez avoir créé un dépôt GitHub nommé "assemblage"
echo    Allez sur: https://github.com/new
echo.
set /p GITHUB_USERNAME="Entrez votre nom d'utilisateur GitHub: "

if "!GITHUB_USERNAME!"=="" (
    echo ❌ Nom d'utilisateur GitHub requis
    pause
    exit /b 1
)

set REPO_URL=https://github.com/!GITHUB_USERNAME!/assemblage.git
echo.
echo ✅ URL du dépôt: !REPO_URL!
echo.

REM Ajouter le remote
git remote remove origin 2>nul
git remote add origin !REPO_URL!
echo ✅ Remote ajouté
echo.

REM Renommer la branche
git branch -M main
echo ✅ Branche renommée en 'main'
echo.

REM Pousser le code
echo 📋 Envoi du code vers GitHub...
echo ⚠️  Vous devrez peut-être entrer vos identifiants GitHub...
echo.
git push -u origin main
if errorlevel 1 (
    echo ❌ Erreur lors de l'envoi vers GitHub
    echo    Vérifiez que:
    echo    1. Votre dépôt GitHub existe et est PUBLIC
    echo    2. Votre nom d'utilisateur est correct
    echo    3. Vous avez accès à Internet
    pause
    exit /b 1
)
echo ✅ Code envoyé vers GitHub
echo.

REM Afficher les instructions finales
cls
echo.
echo ╔════════════════════════════════════════════════════════════════════════════╗
echo ║                                                                            ║
echo ║                    ✅ ETAPE 1 TERMINEE ! ✅                              ║
echo ║                                                                            ║
echo ║                    Votre code est maintenant sur GitHub !                 ║
echo ║                                                                            ║
echo ╚════════════════════════════════════════════════════════════════════════════╝
echo.
echo.

echo 📋 PROCHAINES ETAPES (SUPER SIMPLES):
echo.
echo 1️⃣  Allez sur: https://render.com
echo.
echo 2️⃣  Connectez-vous avec GitHub
echo.
echo 3️⃣  Cliquez sur "New +" puis "Web Service"
echo.
echo 4️⃣  Sélectionnez votre dépôt "assemblage"
echo.
echo 5️⃣  Remplissez les champs:
echo    - Name: assemblage-app
echo    - Build Command: pip install -r requirements.txt
echo    - Start Command: gunicorn app:app
echo    - Plan: Free
echo.
echo 6️⃣  Cliquez sur "Create Web Service"
echo.
echo 7️⃣  Attendez 2-3 minutes
echo.
echo 8️⃣  Votre app sera accessible à:
echo    https://assemblage-app.onrender.com
echo.
echo.

echo ╔════════════════════════════════════════════════════════════════════════════╗
echo ║                                                                            ║
echo ║                  ✅ DEPLOIEMENT AUTOMATISE TERMINE ! ✅                   ║
echo ║                                                                            ║
echo ║              Votre code est sur GitHub, prêt pour Render !               ║
echo ║                                                                            ║
echo ║                    Bonne chance ! 🚀                                      ║
echo ║                                                                            ║
echo ╚════════════════════════════════════════════════════════════════════════════╝
echo.

pause

