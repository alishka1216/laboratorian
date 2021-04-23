from django import forms
from django.core.validators import MinValueValidator, ValidationError
from webapp.models import Product, Order


class ProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'reminder', 'price']


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти' )


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'number', 'adress']