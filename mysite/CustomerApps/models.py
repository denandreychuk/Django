from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomerApp(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', _('Active')
        WARNING = 'WARNING', _('Warning')
        SUSPENDED = 'SUSPENDED', _('Suspended')

    name = models.CharField(max_length=20)
    token = models.CharField(unique=True, max_length=33)
    client = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=Status.choices)

    def __str__(self):
        return self.name + " | " + f"{self.id}"
