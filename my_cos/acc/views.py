import sys

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
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

from .forms import UserRegistrationForm
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
    """ """
    template_name = 'account_activation_sent.html'


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
        return render(request, 'account_activation_invalid.html')

