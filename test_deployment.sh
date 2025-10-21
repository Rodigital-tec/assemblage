#!/bin/bash

echo "🔍 Vérification de la configuration de déploiement..."
echo ""

# Vérifier les fichiers nécessaires
echo "✓ Fichiers de configuration:"
for file in Procfile runtime.txt render.yaml requirements.txt .gitignore .env.example
do
    if [ -f "$file" ]; then
        echo "  ✅ $file"
    else
        echo "  ❌ $file (MANQUANT)"
    fi
done

echo ""
echo "✓ Fichiers principaux:"
for file in app.py wsgi.py models.py
do
    if [ -f "$file" ]; then
        echo "  ✅ $file"
    else
        echo "  ⚠️  $file (optionnel)"
    fi
done

echo ""
echo "✓ Dossiers:"
for dir in static routes
do
    if [ -d "$dir" ]; then
        echo "  ✅ $dir/"
    else
        echo "  ⚠️  $dir/ (optionnel)"
    fi
done

echo ""
echo "✓ Contenu de requirements.txt:"
cat requirements.txt

echo ""
echo "✓ Contenu de Procfile:"
cat Procfile

echo ""
echo "✓ Contenu de runtime.txt:"
cat runtime.txt

echo ""
echo "✅ Configuration de déploiement vérifiée!"
echo ""
echo "Prochaines étapes:"
echo "1. Initialisez Git: git init"
echo "2. Ajoutez les fichiers: git add ."
echo "3. Commitez: git commit -m 'Préparation déploiement'"
echo "4. Poussez vers GitHub/GitLab"
echo "5. Connectez à Render et déployez"

