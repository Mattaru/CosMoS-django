from django.contrib import admin
from django.contrib.auth.models import User

from .models import UserProfile


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass
