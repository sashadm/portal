from django.db import models
from django.contrib.auth.models import User


class Rubric(models.Model):
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name


class BlogEntry(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    title = models.CharField(max_length=50, null=False)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    rubric = models.ForeignKey(Rubric,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.DO_NOTHING, null=True)
    text = models.TextField(blank=False)
    post = models.ForeignKey(BlogEntry, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return f'{self.created_at.strftime("%d-%m-%Y %H:%M ")}  {self.post} -> {self.text}'



