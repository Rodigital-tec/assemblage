@echo off
echo 🔍 Verification de la configuration de deploiement...
echo.

echo ✓ Fichiers de configuration:
if exist Procfile (echo   ✅ Procfile) else (echo   ❌ Procfile MANQUANT)
if exist runtime.txt (echo   ✅ runtime.txt) else (echo   ❌ runtime.txt MANQUANT)
if exist render.yaml (echo   ✅ render.yaml) else (echo   ❌ render.yaml MANQUANT)
if exist requirements.txt (echo   ✅ requirements.txt) else (echo   ❌ requirements.txt MANQUANT)
if exist .gitignore (echo   ✅ .gitignore) else (echo   ❌ .gitignore MANQUANT)
if exist .env.example (echo   ✅ .env.example) else (echo   ❌ .env.example MANQUANT)

echo.
echo ✓ Fichiers principaux:
if exist app.py (echo   ✅ app.py) else (echo   ⚠️  app.py MANQUANT)
if exist wsgi.py (echo   ✅ wsgi.py) else (echo   ⚠️  wsgi.py optionnel)
if exist models.py (echo   ✅ models.py) else (echo   ⚠️  models.py optionnel)

echo.
echo ✓ Dossiers:
if exist static (echo   ✅ static/) else (echo   ⚠️  static/ optionnel)
if exist routes (echo   ✅ routes/) else (echo   ⚠️  routes/ optionnel)

echo.
echo ✓ Contenu de requirements.txt:
type requirements.txt

echo.
echo ✓ Contenu de Procfile:
type Procfile

echo.
echo ✓ Contenu de runtime.txt:
type runtime.txt

echo.
echo ✅ Configuration de deploiement verifiee!
echo.
echo Prochaines etapes:
echo 1. Initialisez Git: git init
echo 2. Ajoutez les fichiers: git add .
echo 3. Commitez: git commit -m "Preparation deploiement"
echo 4. Poussez vers GitHub/GitLab
echo 5. Connectez a Render et deployez
pause

