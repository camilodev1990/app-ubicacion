# apps/ubicacion/forms.py
from django import forms
from .models import Ubicacion

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = [
            "departamento",
            "ciudad",
            "via",
            "numero1",
            "numero2",
            "tipo_ubicacion",
            "nombre_ubicacion",
            "detalle_adicional",
        ]
        widgets = {
            "departamento": forms.Select(attrs={"class": "form-select"}),
            "ciudad": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ciudad"}),
            "via": forms.Select(attrs={"class": "form-select"}),
            "numero1": forms.TextInput(attrs={"class": "form-control", "placeholder": "Número o nombre de vía"}),
            "numero2": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nomenclatura"}),
            "tipo_ubicacion": forms.Select(attrs={"class": "form-select"}),
            "nombre_ubicacion": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre de la ubicación"}),
            "detalle_adicional": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Detalles adicionales (opcional)"}),
        }
