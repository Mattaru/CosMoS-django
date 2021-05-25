from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html


class UserForm(UserCreationForm):
    password1 = forms.CharField(
        label=_('Password'),
        help_text=format_html(
            '<ul>'
            '<li>{}</li>'
            '<li>{}</li>'
            '<li>{}</li>'
            '<li>{}</li>'
            '</ul>',
            _('Your password can’t be too similar to your other personal information.'),
            _(' Your password must contain at least 8 characters.'),
            _(' Your password can’t be a commonly used password.'),
            _(' Your password can’t be entirely numeric.')
        ),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-general form-input',
                'placeholder': _('Enter password'),
                'required': True
            }
        )
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        help_text=_('Enter the same password as before, for verification.'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-general form-input',
                'placeholder': _('Confirm your password'),
                'required': True
            }
        )
    )

    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-general form-input',
                    'placeholder': _('Enter username'),
                    'required': True,
                })
        }
