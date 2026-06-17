from django.conf import settings
from django.core.mail import send_mail
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
            mascota = form.save()

            perfil_url = request.build_absolute_uri(
                f'/mascota/{mascota.id}/'
            )

            mensaje = f"""
            Nueva mascota registrada

            Nombre: {mascota.nombre}
            Raza: {mascota.raza}
            Edad: {mascota.edad}
            Dueño: {mascota.duenio}
            Teléfono: {mascota.telefono}

            Perfil: 
            {perfil_url}
            """
            try:
                send_mail(
                    subject=f"Nueva mascota registrada: {mascota.nombre}",
                    message=mensaje,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['idsmascotas@gmail.com'],
                    fail_silently=False,
                )
            except Exception as e:
                print("ERROR CORREO:", str(e))
            return redirect('mascota_registrada', id=mascota.id)
    else:
        form = MascotaForm()

    return render(request, 'registrar_mascota.html', {'form': form})

def mascota_registrada(request, id):
    mascota = Mascota.objects.get(id=id)
    perfil_url = request.build_absolute_uri(f'/mascota/{mascota.id}/')
    return render(request, 'mascota_registrada.html', {
        'mascota': mascota,
        'perfil_url': perfil_url
    })