from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name=_('User'), blank=True, null=True, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(_('email confirmed'), default=False)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def __str__(self):
        return f'{self.user}'

    def get_absolute_url(self):
        return reverse('acc:profile_detail', args=[self.id])
