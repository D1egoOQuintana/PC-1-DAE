from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacto
from .forms import ContactoForm
import csv
from django.http import HttpResponse

def listar_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'contactos/lista.html', {'contactos': contactos})

def crear_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_contactos')
    else:
        form = ContactoForm()
    return render(request, 'contactos/formulario.html', {'form': form})

def editar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('listar_contactos')
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'contactos/formulario.html', {'form': form})

def eliminar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == 'POST':
        contacto.delete()
        return redirect('listar_contactos')
    return render(request, 'contactos/eliminar.html', {'contacto': contacto})

def exportar_contactos_csv(request):
    # Crear la respuesta HTTP con el tipo de contenido CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contactos.csv"'

    # Crear el escritor CSV
    writer = csv.writer(response)
    writer.writerow(['Nombre', 'Email', 'Teléfono', 'Dirección'])  # Encabezados

    # Escribir los datos de los contactos
    contactos = Contacto.objects.all()
    for contacto in contactos:
        writer.writerow([contacto.nombre, contacto.email, contacto.telefono, contacto.direccion])

    return response