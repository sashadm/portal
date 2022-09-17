from django.db import models


class Rubric(models.Model):
    name = models.CharField(max_length=30, null=False)


class BlogEntry(models.Model):
    '''title,text,data,hashtag,rubrika'''
    title = models.CharField(max_length=50, null=False)
    text =  models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    rubric = models.ForeignKey(Rubric,null=True,on_delete=models.SET_NULL)


