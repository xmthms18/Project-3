from django.contrib.auth.models import AbstractUser
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)

class CustomUser(AbstractUser):
    # Add custom fields here if needed
    # For example:
    # birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
      return self.username