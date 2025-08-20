from rest_framework import serializers
from .models import Product

# 🔄 ProductSerializer : convertit le modèle Product en JSON et inversement
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Tous les champs sont exposés via l'API
