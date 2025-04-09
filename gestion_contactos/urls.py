from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contactos.urls')),  # Ruta principal redirige a la app 'contactos'
]