from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Mascota


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'duenio',
        'telefono',
        'raza',
        'edad',
        'ver_qr',
    )

    search_fields = (
        'nombre',
        'duenio',
        'telefono',
    )

    list_filter = (
        'raza',
    )

    def ver_qr(self, obj):
        url = reverse('perfil_mascota', args=[obj.id])
        return format_html(
            '<a class="button" href="{}" target="_blank">Ver QR</a>',
            url
        )

    ver_qr.short_description = "QR"