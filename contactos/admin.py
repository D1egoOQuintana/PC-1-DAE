from django.contrib import admin
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'direccion', 'creado')
    search_fields = ('nombre', 'email')
    list_filter = ('creado',)
    ordering = ('-creado',)