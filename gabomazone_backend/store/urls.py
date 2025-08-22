# store/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet, CategoryViewSet, SellerViewSet,
    ProductViewSet, ReviewViewSet,
    CartViewSet, CartItemViewSet, WishlistViewSet,
)
from .views_auth import RegisterCustomerView, RegisterVendorView

# Vues JWT fournies par SimpleJWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # login -> access + refresh
    TokenRefreshView,     # refresh -> nouveau access
    TokenVerifyView,      # (optionnel) vérifier un token
)

router = DefaultRouter()
router.register("users", UserViewSet)
router.register("categories", CategoryViewSet)
router.register("sellers", SellerViewSet)
router.register("products", ProductViewSet)
router.register("reviews", ReviewViewSet)
router.register("carts", CartViewSet)
router.register("cart-items", CartItemViewSet)
router.register("wishlists", WishlistViewSet)

urlpatterns = [
    # Auth: inscription
    path("auth/register/customer/", RegisterCustomerView.as_view(), name="register-customer"),
    path("auth/register/vendor/", RegisterVendorView.as_view(), name="register-vendor"),

    # Auth: JWT (login / refresh / verify)
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/token/verify/", TokenVerifyView.as_view(), name="token_verify"),

    # Le reste des routes API
    path("", include(router.urls)),
]
