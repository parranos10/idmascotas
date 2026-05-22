from django.shortcuts import render, redirect
from .forms import MascotaForm
from .models import Mascota
import qrcode
from io import BytesIO
import base64

def perfil_mascota(request, id):

    mascota = Mascota.objects.get(id=id)

    qr_texto = request.build_absolute_uri()

    qr = qrcode.make(qr_texto)

    buffer = BytesIO()

    qr.save(buffer, format='PNG')

    qr_base64 = base64.b64encode(buffer.getvalue()).decode()

    return render(request, 'perfil_mascota.html', {
        'mascota': mascota,
        'qr_code': qr_base64
    })

def home(request):
    return render(request, 'home.html')

def registrar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MascotaForm()

    return render(request, 'registrar_mascota.html', {'form': form})