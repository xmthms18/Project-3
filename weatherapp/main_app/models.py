from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields here if needed
    # For example:
    # birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.username

