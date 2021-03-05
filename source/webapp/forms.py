from django import forms
from django.core.validators import MinValueValidator


class ProductForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=3000, required=True)
    category = forms.CharField(max_length=200)
    reminder = forms.IntegerField(validators=[MinValueValidator(0)])
    price = forms.DecimalField(decimal_places=2, max_digits=7)
