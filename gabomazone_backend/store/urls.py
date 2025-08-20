from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# 🔹 Router automatique pour gérer toutes les routes CRUD
router = DefaultRouter()
router.register(r'products', ProductViewSet)  # /api/products/

urlpatterns = [
    path('', include(router.urls)),  # Inclut toutes les routes générées
]
