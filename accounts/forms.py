from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import TextInput, PasswordInput

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter username'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter first name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter last name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter email address'
                }
            ),
        }
        # Menimpa widgets password1 dan password2
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter password'
            }
        )
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Re-enter password'
            }
        )
        
class LoginForm(AuthenticationForm):
    
    username = forms.CharField(
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter username'
            }
        )
    )
    password = forms.CharField(
        widget=PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter password'
            }
        )
    )