from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image

class Mascota(models.Model):

    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()
    duenio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    informacion = models.TextField(blank=True)

    foto = models.ImageField(upload_to='mascotas/', blank=True, null=True)

    qr = models.ImageField(upload_to='qr/', blank=True)

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        qr_texto = f"https://petqr.onrender.com/{self.id}/"

        qr_img = qrcode.make(qr_texto)

        canvas = BytesIO()

        qr_img.save(canvas, format='PNG')

        nombre_archivo = f'qr_mascota_{self.id}.png'

        self.qr.save(nombre_archivo, File(canvas), save=False)

        super().save(*args, **kwargs)

    
    def telefono_whatsapp(self):
        numero = self.telefono.strip()
        numero = self.telefono.replace(" ", "").replace("+", "")

        if numero.startswith("0"):
            numero = "593" + numero[1:]
        elif numero.startswith("9") and len(numero) == 9:
            numero = "593" + numero
        return numero 


    def __str__(self):
        return self.nombre