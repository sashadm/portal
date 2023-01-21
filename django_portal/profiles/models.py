from django.db import models
from django.contrib.auth.models import User

class Profiles(models.Model):
    user = models.OneToOneField(User, blank=True, related_name='profile',on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to='upload/', null=True)
    head = models.ImageField(upload_to='upload/', null=True)
    description = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=15, default='Minsk')
