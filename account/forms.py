from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), label='', max_length=20)
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), label='', max_length=20)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), label='', max_length=32)
    password1 = forms.CharField(label='',
                                widget=(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})),
                                help_text=None)
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
                                help_text=password_validation.password_validators_help_text_html())
    username = forms.CharField(label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        max_length=32,
        help_text='Required. 32 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={'unique': "A user with that username already exists."},
    )

    class Meta:
        model = User
        fields = ["username", 'first_name', 'last_name', "email", "password1", "password2"]