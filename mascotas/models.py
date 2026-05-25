from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()
    duenio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    informacion = models.TextField(blank=True)
    foto = models.ImageField(upload_to='mascotas/', blank=True, null=True)

    def telefono_whatsapp(self):
        numero = self.telefono.strip()
        numero = numero.replace(" ", "").replace("-", "").replace("+", "")

        if numero.startswith("09"):
            numero = "593" + numero[1:]
        elif numero.startswith("9") and len(numero) == 9:
            numero = "593" + numero

        return numero

    def __str__(self):
        return self.nombre