from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from acc.views import ProfileDetail


app_name = 'acc'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
]