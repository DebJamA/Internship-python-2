from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    # remove password field from the form
    # so default message and redirect are not shown
    password = None

    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name')
