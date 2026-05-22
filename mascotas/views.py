from django.shortcuts import render, redirect
from .forms import MascotaForm
from .models import Mascota

def perfil_mascota(request, id):
    mascota = Mascota.objects.get(id=id)
    return render(request, 'perfil_mascota.html', {'mascota': mascota})

def home(request):
    mascotas = Mascota.objects.all()
    return render(request, 'home.html', {'mascotas': mascotas})

def registrar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MascotaForm()

    return render(request, 'registrar_mascota.html', {'form': form})