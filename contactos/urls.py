from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_contactos, name='listar_contactos'),  # Ruta principal
    path('nuevo/', views.crear_contacto, name='crear_contacto'),
    path('editar/<int:id>/', views.editar_contacto, name='editar_contacto'),
    path('eliminar/<int:id>/', views.eliminar_contacto, name='eliminar_contacto'),
    path('exportar/', views.exportar_contactos_csv, name='exportar_contactos'),  # Ruta para exportar contactos
]