# store/serializers_auth.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Seller, Cart, Wishlist

class RegisterCustomerSerializer(serializers.ModelSerializer):
    """Inscription client classique (User + création du Panier & Wishlist)."""
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "last_name"]

    def create(self, validated_data):
        # Création du user + hash du password
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        # Crée automatiquement un panier & une wishlist pour ce client
        Cart.objects.get_or_create(user=user)
        Wishlist.objects.get_or_create(user=user)

        return user


class RegisterVendorSerializer(RegisterCustomerSerializer):
    """Inscription vendeur : crée aussi son profil Seller (boutique)."""
    store_name = serializers.CharField(write_only=True, max_length=150)
    description = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta(RegisterCustomerSerializer.Meta):
        fields = RegisterCustomerSerializer.Meta.fields + ["store_name", "description"]

    def create(self, validated_data):
        # Extrait les champs boutique
        store_name = validated_data.pop("store_name")
        description = validated_data.pop("description", "")

        # Crée d’abord l’utilisateur via la logique parent
        user = super().create(validated_data)

        # Crée le profil vendeur lié
        Seller.objects.create(user=user, store_name=store_name, description=description)

        return user
