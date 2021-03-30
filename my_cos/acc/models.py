from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, verbose_name='User profile', on_delete=models.CASCADE,
                             null=True, blank=True, related_name='user_profile')

    def __str__(self):
        return self.user


def create_user_profile(sender, **kwargs):
    """
    Create a new UserProfile for the User(sender).
    """
    user = kwargs['instance']
    if kwargs['created']:
        user_profile = UserProfile(user=user)
        user_profile.save()


post_save.connect(create_user_profile, sender=User)