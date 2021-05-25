from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .forms import UserForm


class RegistrationView(FormView):
    """New User creation view."""
    form_class = UserForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('app:main_page')

    # def get_context_data(self, *args, **kwargs):
    #     context = super(RegistrationView, self).get_context_data(*args, **kwargs)
    #     context['form'] = UserForm()
    #
    #     return context
    #
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #
    #     if form.is_valid():
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password1')
    #         user = User(username=username, password=password)
    #
    #         return HttpResponseRedirect('/success/')
    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        login(self.request, authenticate(username=username, password=raw_password))

        return super(RegistrationView, self).form_valid(form)