from django.db import models
from django.contrib.auth.models import User


class ForumSection(models.Model):
    title = models.CharField(max_length=50, null=False)


class ForumTheme(models.Model):
    title = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    section = models.ForeignKey(ForumSection, null=True, on_delete=models.SET_NULL)


class ForumMessage(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, related_name='messages', on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    theme = models.ForeignKey(ForumTheme, null=True, on_delete=models.SET_NULL)

