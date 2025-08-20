#!/bin/bash

# ================================
# 🚀 Gabomazone Dev Launcher
# ================================

echo "==================================="
echo "    🚀 Bienvenue dans Gabomazone"
echo "==================================="

# Activer venv Python
if [ -d "venv" ]; then
    echo "📦 Activation de l'environnement Python..."
    source venv/bin/activate
else
    echo "❌ Aucun environnement virtuel trouvé !"
    exit 1
fi

# Lancer le backend Django
echo "🟢 Lancement du backend Django sur le port 8000..."
cd gabomazone_backend
python manage.py runserver 0.0.0.0:8000 &
BACKEND_PID=$!
cd ..

# Lancer le frontend React
echo "🟢 Lancement du frontend React sur le port 3000..."
cd gabomazone-frontend
npm start &
FRONTEND_PID=$!
cd ..

# Attente
echo "==================================="
echo " ✅ Gabomazone est prêt !"
echo " - Backend : http://127.0.0.1:8000"
echo " - Frontend : http://127.0.0.1:3000"
echo "==================================="

# Empêche le script de s'arrêter
wait $BACKEND_PID $FRONTEND_PID
