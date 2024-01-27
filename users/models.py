from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    role = models.CharField(max_length=255,
                            choices=(("operator", "operator"), ("driver", "driver"), ("owner", "owner")))

    class Meta:
        verbose_name_plural = 'CustomUser'
