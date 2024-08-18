from django.db import models

from .user import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    biography = models.TextField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
