from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

# 🛠️ ProductViewSet : API complète (CRUD) pour Product
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()          # Tous les produits
    serializer_class = ProductSerializer      # Sérialiseur associé
