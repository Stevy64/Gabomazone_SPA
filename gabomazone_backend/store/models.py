from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# -------------------
# 1) Catégorie de produit
# -------------------
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


# -------------------
# 2) Vendeur
# -------------------
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # lien avec le compte utilisateur
    store_name = models.CharField(max_length=150, unique=True)   # nom de la boutique
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)         # date de création

    def __str__(self):
        return self.store_name


# -------------------
# 3) Produit
# -------------------
class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="products")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.seller.store_name}"


# -------------------
# 4) Avis des clients
# -------------------
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ⚠️ Ici on corrige ton erreur : IntegerField + validateurs
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]  # note entre 1 et 5
    )
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.rating})"


# -------------------
# 5) Panier
# -------------------
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Panier de {self.user.username}"


# -------------------
# 6) Éléments du panier
# -------------------
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"


# -------------------
# 7) Liste de souhaits
# -------------------
class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f"Wishlist de {self.user.username}"
