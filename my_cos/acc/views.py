from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# from acc.models import UserProfile


class ProfileDetail(DetailView, LoginRequiredMixin):
    model = User
    template_name = 'accounts/administration/admin_detail.html'