from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacto
from .forms import ContactoForm

def listar_contactos(request):
    query = request.GET.get('q')  # Obtén el término de búsqueda desde la URL
    if query:
        contactos = Contacto.objects.filter(nombre__icontains=query)  # Filtra por nombre
    else:
        contactos = Contacto.objects.all()  # Muestra todos los contactos
    return render(request, 'contactos/lista.html', {'contactos': contactos, 'query': query})

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
    return render(request, 'contactos/formulario.html', {'form': form, 'contacto': contacto})

def eliminar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == 'POST':
        contacto.delete()
        return redirect('listar_contactos')
    return render(request, 'contactos/eliminar.html', {'contacto': contacto})