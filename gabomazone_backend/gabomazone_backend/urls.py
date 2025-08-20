from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),        # Interface d'administration Django
    path('api/', include('store.urls')),    # Toutes les API de l'app store
]
