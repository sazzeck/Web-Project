from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Users


class SingUpForm(UserCreationForm):
    username = forms.CharField(
        label='Login',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )
    user_type = forms.ChoiceField(
        label='User Type',
        choices=Users.UserType.choices,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Users
        fields = (
            'username',
            'password1',
            'password2',
            'user_type'
        )


class SingInForm(AuthenticationForm):
    username = forms.CharField(
        label='username',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )
