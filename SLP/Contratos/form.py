from django import forms

from.models import (
    CatContinente,
    CatPais,
    CatEstados,
    CatPlaza
)


class registrarplaza(forms.ModelForm):
    class Meta:
        model = CatPlaza
        fields = '__all__'