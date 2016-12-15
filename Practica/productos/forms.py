from django import forms
from productos.models import Producto


class ProductForm(forms.ModelForm):
    class Meta:
        model = Producto