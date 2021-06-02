from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView
)

from app.forms import OneRowSearch
from .forms import LoginForm,ResetPasswordForm, PasswordSetForm
from .views import ActivationSent, RegistrationView, activate
from my_cos.settings import FROM_EMAIL


app_name = 'acc'

urlpatterns = [
    path('account/login/', LoginView.as_view(
        template_name='accounts/login.html',
        authentication_form=LoginForm,
        extra_context={
            'search_form': OneRowSearch(),
        },
    ), name='login'),
    path('account/logout/', LogoutView.as_view(), name='logout'),
    path('account/registration/', RegistrationView.as_view(
        extra_context={
            'search_form': OneRowSearch(),
        },
    ), name='registration'),
    path('account/account_activation_sent/', ActivationSent.as_view(), name='account_activation_sent'),
    path('account/activate/<uidb64>/<token>/', activate, name='activate'),
    path('account/password_reset/', PasswordResetView.as_view(
        template_name='accounts/password_reset.html',
        form_class=ResetPasswordForm,
        from_email=FROM_EMAIL,
        success_url=reverse_lazy('acc:password_reset_done'),
        email_template_name='password_reset_email.html',
        extra_context={
            'search_form': OneRowSearch(),
        },
    ), name='password_reset'),
    path('account/password_reset/done/', PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html',
        extra_context={
            'search_form': OneRowSearch(),
        },
    ), name='password_reset_done'),
    path('account/password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        form_class=PasswordSetForm,
        success_url=reverse_lazy('acc:password_reset_complete'),
        extra_context={
            'search_form': OneRowSearch(),
        },
    ), name='password_reset_confirm'),
    path('account/password_reset_complete/', PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html',
        extra_context={
            'search_form': OneRowSearch(),
        },
    ), name='password_reset_complete')
]
