#!/bin/bash

# 🚀 Script de réparation pour Gabomazone Frontend React

echo "============================================="
echo " 🔧 Vérification et réparation du projet React"
echo "============================================="

# 1️⃣ Vérifier si npm est installé
if ! command -v npm &> /dev/null
then
    echo "❌ npm n'est pas installé. Installe Node.js et npm avant de continuer."
    exit 1
fi

# 2️⃣ Supprimer node_modules et package-lock.json pour repartir propre
echo "🧹 Suppression de node_modules et package-lock.json..."
rm -rf node_modules package-lock.json

# 3️⃣ Réinstaller toutes les dépendances
echo "📦 Réinstallation des dépendances..."
npm install

# 4️⃣ Installer react-router-dom si manquant ou corriger la version
echo "🔗 Installation / mise à jour de react-router-dom..."
npm install react-router-dom@6

# 5️⃣ Lancer le serveur de développement
echo "🏃‍♂️ Démarrage du serveur de développement..."
npm start

echo "✅ Script terminé ! Si tout va bien, ton projet React devrait se lancer sans erreur."
