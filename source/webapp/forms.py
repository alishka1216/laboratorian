from django import forms
from django.core.validators import MinValueValidator
from webapp.models import category_choices

class ProductForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=3000, required=True, widget=forms.Textarea)
    category = forms.ChoiceField(choices=category_choices)
    reminder = forms.IntegerField(validators=[MinValueValidator(0)])
    price = forms.DecimalField(decimal_places=2, max_digits=7)
