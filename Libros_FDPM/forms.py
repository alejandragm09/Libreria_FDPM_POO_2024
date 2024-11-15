from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_publicacion', 'isbn']
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
        }