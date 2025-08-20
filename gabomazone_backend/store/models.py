from django.db import models

# 🛍️ Modèle Product : représente un produit du catalogue Gabomazone
class Product(models.Model):
    name = models.CharField(max_length=255)  # Nom du produit
    description = models.TextField()          # Description détaillée
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Prix
    stock = models.PositiveIntegerField(default=0)  # Quantité disponible
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création
    updated_at = models.DateTimeField(auto_now=True)      # Date de dernière modification

    def __str__(self):
        return self.name  # Représentation en string pour l’admin
