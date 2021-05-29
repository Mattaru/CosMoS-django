import sys

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_text
from django.utils.translation import gettext_lazy as _
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from .forms import ResetPasswordForm, UserRegistrationForm
from core.tokens import account_activation_token
from my_cos.settings import FROM_EMAIL


class RegistrationView(FormView):
    """New User creation view."""
    form_class = UserRegistrationForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('acc:account_activation_sent')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        subject = 'Activate Your Account'
        message = render_to_string('account_activation_email.html', context={
            'user': user.username,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            'protokol': 'http'
        })

        try:
            send_mail(
                subject,
                message,
                FROM_EMAIL,
                [user.email],
                fail_silently=False
            )
        except:
            e = sys.exc_info()
            print(f'Sending error: {e}')

        return super(RegistrationView, self).form_valid(form)


class ActivationSent(TemplateView):
    """View with the activation sent message."""
    template_name = 'accounts/account_activation_sent.html'


# class PasswordResetRequestView(PasswordResetView):
#     """ """
#     template_name = 'accounts/password_reset.html'
#     form_class = ResetPasswordForm
#     from_email = FROM_EMAIL
#     success_url = reverse_lazy('acc:password_reset_done')
#
#     def form_valid(self, form):
#         email = form.cleaned_data['email']
#         current_site = get_current_site(self.request)
#         user = User.objects.filter(email=email)
#
#         if user.exists():
#             subject = 'Password Reset Requested'
#             message = render_to_string('password_reset_email.html', context={
#                 'user': user.first().username,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.first().pk)),
#                 'token': account_activation_token.make_token(user.first()),
#                 'protokol': 'http',
#             })
#
#             try:
#                 send_mail(
#                     subject,
#                     message,
#                     FROM_EMAIL,
#                     [user.email],
#                     fail_silently=False
#                 )
#             except:
#                 e = sys.exc_info()
#                 print(f'Sending error: {e}')
#
#         return super(PasswordResetRequestView, self).form_valid(form)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.userprofile.email_confirmed = True
        user.save()
        login(request, user)

        return HttpResponseRedirect(reverse_lazy('app:main_page'))
    else:
        return render(request, 'accounts/account_activation_invalid.html')

