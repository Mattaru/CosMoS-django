from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-general form-auth-input',
                'placeholder': _('Username'),
                'required': True,
            }
        )
    )
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-general form-auth-input',
                'placeholder': _('Password'),
                'required': True
            }
        )
    )


class UserRegistrationForm(UserCreationForm):
    username = forms.RegexField(
        label=_('Username'),
        regex=r'^[\w.@+-]+$',
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")
        },
        help_text=format_html(
            '<ul><li>{}</li></ul>',
            _('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')
        ),
        widget=forms.TextInput(
            attrs={
                'class': 'form-general form-auth-input',
                'placeholder': _('Username'),
                'required': True,
            }
        )
    )
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
                'class': 'form-general form-auth-input',
                'placeholder': _('Enter password'),
                'required': True
            }
        )
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        help_text=format_html(
            '<ul><li>{}</li></ul>',
            _('Enter the same password as before, for verification.')
        ),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-general form-auth-input',
                'placeholder': _('Confirm your password'),
                'required': True
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'email': forms.TextInput(
                attrs={
                    'class': 'form-general form-auth-input',
                    'placeholder': _('example@dot.com'),
                    'required': True,
                }),
        }
