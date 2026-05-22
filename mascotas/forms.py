from django import forms
from .models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = [
            'nombre',
            'raza',
            'edad',
            'duenio',
            'telefono',
            'informacion',
            'foto',
        ]

        labels = {
            'nombre': 'Nombre de la mascota',
            'raza': 'Raza',
            'edad': 'Edad',
            'duenio': 'Nombre del dueño',
            'telefono': 'Teléfono de contacto',
            'informacion': 'Información importante',
            'foto': 'Foto de la mascota',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Max'
            }),
            'raza': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Golden Retriever'
            }),
            'edad': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 3'
            }),
            'duenio': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Jonathan Guaygua'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 0987654321'
            }),
            'informacion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Ej: Es alérgico, toma medicación, es nervioso, etc.'
            }),
            'foto': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }