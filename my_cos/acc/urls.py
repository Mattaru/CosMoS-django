from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView

from django.contrib.auth import views as auth_views

from .forms import LoginForm, ResetPasswordForm
from .views import ActivationSent, RegistrationView, activate
from my_cos.settings import FROM_EMAIL


app_name = 'acc'

urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='accounts/login.html',
        authentication_form=LoginForm,
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),

    path('account_activation_sent/', ActivationSent.as_view(), name='account_activation_sent'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='accounts/password_reset.html',
        from_email=FROM_EMAIL
    ), name='password_reset')
]
