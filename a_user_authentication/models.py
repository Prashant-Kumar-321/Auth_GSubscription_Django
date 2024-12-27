from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.URLField(max_length=150, null=True)
    full_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=50, null=True)

    def __str__(self): 
        return f"{self.full_name}: @{self.user.username}"