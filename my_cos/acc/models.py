from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.urls import reverse


class UserProfile(models.Model):
    user = models.ForeignKey(User, verbose_name='User', blank=True, null=True, on_delete=models.CASCADE,
                             related_name='user_profile')

    def __str__(self):
        return f'{self.user}'

    def get_absolute_url(self):
        return reverse('acc:profile_detail', args=[self.id])


def create_user_profile(sender, **kwargs):
    """
    Create a new UserProfile for the User(sender).
    """
    user = kwargs['instance']
    if kwargs['created']:
        user_profile = UserProfile(user=user)
        user_profile.save()


post_save.connect(create_user_profile, sender=User)
