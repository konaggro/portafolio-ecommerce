from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            "nombre",
            "descripcion",
            "precio",
            "stock",
            "disponible",
            "categoria",
        ]

    def clean_precio(self):
        precio = self.cleaned_data["precio"]

        if precio <= 0:
            raise forms.ValidationError(
                "El precio debe ser mayor que 0."
            )

        return precio