from django import forms

from Web.models import (
    DatProveedor
)


class proveedores(forms.ModelForm):
    class Meta:
        model = DatProveedor
        fields = '__all__'
