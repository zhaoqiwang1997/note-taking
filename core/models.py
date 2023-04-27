from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customer_set',
        verbose_name='groups',
    )

    # specify a unique related_name for the user_permissions field
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customer_set',
        verbose_name='permissions',
    )