from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Category, Seller, Product, Review, Cart, CartItem, Wishlist
from .serializers import (
    UserSerializer, CategorySerializer, SellerSerializer,
    ProductSerializer, ReviewSerializer,
    CartSerializer, CartItemSerializer, WishlistSerializer
)

# --------------------
# Utilisateurs
# --------------------
class UserViewSet(viewsets.ModelViewSet):
    """
    Permet de gérer les utilisateurs (clients et vendeurs).
    Accessible en lecture par tous, mais certaines actions
    peuvent être restreintes plus tard (IsAdmin).
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


# --------------------
# Catégories
# --------------------
class CategoryViewSet(viewsets.ModelViewSet):
    """
    CRUD des catégories de produits.
    Exemple : Mode, High-tech, Maison…
    Lecture publique autorisée.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


# --------------------
# Vendeurs
# --------------------
class SellerViewSet(viewsets.ModelViewSet):
    """
    CRUD des vendeurs (boutiques).
    - Un vendeur est lié à un utilisateur (OneToOne).
    - Lors de la création, le vendeur correspond à l’utilisateur connecté.
    """
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# --------------------
# Produits
# --------------------
class ProductViewSet(viewsets.ModelViewSet):
    """
    CRUD des produits :
    - Lecture publique (tout le monde peut voir les produits)
    - Création/édition réservées aux vendeurs connectés
    - Lors d’un POST, le produit est automatiquement
      rattaché au vendeur connecté
    """
    queryset = Product.objects.all().order_by("-created_at")
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        seller = get_object_or_404(Seller, user=self.request.user)
        serializer.save(seller=seller)


# --------------------
# Avis Produits
# --------------------
class ReviewViewSet(viewsets.ModelViewSet):
    """
    Gestion des avis clients :
    - Chaque client peut poster un avis (rating + commentaire)
    - L’utilisateur connecté est automatiquement associé à l’avis
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# --------------------
# Panier
# --------------------
class CartViewSet(viewsets.ModelViewSet):
    """
    Gestion du panier d’un utilisateur.
    - Chaque utilisateur a son propre panier (lié à son compte).
    - Lecture et modification réservées au propriétaire.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# --------------------
# Éléments du Panier
# --------------------
class CartItemViewSet(viewsets.ModelViewSet):
    """
    Gestion des éléments du panier (produits ajoutés).
    - L’utilisateur connecté peut ajouter, modifier ou supprimer
      ses articles dans son panier.
    """
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)


# --------------------
# Wishlist (Liste de souhaits)
# --------------------
class WishlistViewSet(viewsets.ModelViewSet):
    """
    Gestion des listes de souhaits :
    - Chaque utilisateur a une seule wishlist (OneToOne).
    - Il peut y ajouter/supprimer des produits.
    """
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# --------------------
# Droits vendeur/client
# --------------------
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("-created_at")
    serializer_class = ProductSerializer

    def get_permissions(self):
        # Lecture publique; écriture = vendeur connecté uniquement
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        # Le vendeur connecté ajoute son produit
        seller = get_object_or_404(Seller, user=self.request.user)
        serializer.save(seller=seller)

    def perform_update(self, serializer):
        # Optionnel: empêcher un vendeur de modifier un produit qui n’est pas à lui
        instance = self.get_object()
        seller = get_object_or_404(Seller, user=self.request.user)
        if instance.seller_id != seller.id:
            raise PermissionError("Vous ne pouvez modifier que vos propres produits.")
        serializer.save()
