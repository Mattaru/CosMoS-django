from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .forms import UserRegistrationForm


class RegistrationView(FormView):
    """New User creation view."""
    form_class = UserRegistrationForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('app:main_page')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        login(self.request, authenticate(username=username, password=raw_password))

        return super(RegistrationView, self).form_valid(form)