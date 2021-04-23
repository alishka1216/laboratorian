from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import PasswordInput


class UserRegisterForm(UserCreationForm):
    email = forms.CharField(max_length=30, required=True)

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean(self):
        super(UserRegisterForm, self).clean()
        if not self.cleaned_data.get('first_name') and not self.cleaned_data.get('last_name'):
            raise ValidationError('First name or last name should be registered.')
