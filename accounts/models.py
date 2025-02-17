from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    avatar = models.ImageField(upload_to="avatars/",blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    birth_day = models.DateField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "profile")
    def __str__(self) -> str:
        return f"{self.user.username}'s profile"



