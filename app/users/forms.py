from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label='Login',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )
    password2 = forms.CharField(
        label='Repeat Password',
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'password1',
            'password2',
            'type_user',
        )


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Login',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )
