from django import forms
from django.core.validators import MinValueValidator, ValidationError
from webapp.models import Product



class ProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'reminder', 'price']