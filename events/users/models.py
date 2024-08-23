from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username
