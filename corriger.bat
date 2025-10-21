@echo off
REM ╔════════════════════════════════════════════════════════════════════════════╗
REM ║                                                                            ║
REM ║                    🔧 CORRECTION AUTOMATIQUE 🔧                           ║
REM ║                                                                            ║
REM ║                    Erreur GitHub: "failed to push some refs"              ║
REM ║                                                                            ║
REM ╚════════════════════════════════════════════════════════════════════════════╝

setlocal enabledelayedexpansion

cls
echo.
echo ╔════════════════════════════════════════════════════════════════════════════╗
echo ║                                                                            ║
echo ║                    🔧 CORRECTION AUTOMATIQUE 🔧                           ║
echo ║                                                                            ║
echo ║                    Erreur GitHub: "failed to push some refs"              ║
echo ║                                                                            ║
echo ╚════════════════════════════════════════════════════════════════════════════╝
echo.
echo.

REM Étape 1: Vérifier Git
echo 📋 Étape 1/3: Vérification de Git...
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git n'est pas installé.
    pause
    exit /b 1
)
echo ✅ Git est installé
echo.

REM Étape 2: Télécharger les fichiers du dépôt
echo 📋 Étape 2/3: Téléchargement des fichiers du dépôt GitHub...
git pull origin main --allow-unrelated-histories
if errorlevel 1 (
    echo ⚠️  Erreur lors du téléchargement
    echo    Essayez de résoudre les conflits manuellement
    pause
    exit /b 1
)
echo ✅ Fichiers téléchargés
echo.

REM Étape 3: Envoyer le code
echo 📋 Étape 3/3: Envoi du code vers GitHub...
git push -u origin main
if errorlevel 1 (
    echo ❌ Erreur lors de l'envoi
    echo    Vérifiez que:
    echo    1. Votre dépôt GitHub existe et est PUBLIC
    echo    2. Vous avez accès à Internet
    echo    3. Vos identifiants GitHub sont corrects
    pause
    exit /b 1
)
echo ✅ Code envoyé vers GitHub
echo.

REM Afficher le succès
cls
echo.
echo ╔════════════════════════════════════════════════════════════════════════════╗
echo ║                                                                            ║
echo ║                    ✅ ERREUR CORRIGEE ! ✅                               ║
echo ║                                                                            ║
echo ║                    Votre code est maintenant sur GitHub !                 ║
echo ║                                                                            ║
echo ╚════════════════════════════════════════════════════════════════════════════╝
echo.
echo.

echo 📋 PROCHAINES ETAPES:
echo.
echo 1. Allez sur: https://render.com
echo 2. Connectez-vous avec GitHub
echo 3. Cliquez sur "New +" puis "Web Service"
echo 4. Sélectionnez votre dépôt "assemblage"
echo 5. Configurez et déployez
echo.

pause

