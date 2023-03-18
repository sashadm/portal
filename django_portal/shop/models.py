from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=50, null=False)


class Rubric(models.Model):
    title = models.CharField(max_length=50, null=False)
    section = models.ForeignKey(Section, related_name='rubrics',null=True, on_delete=models.SET_NULL)


class Product(models.Model):
    title = models.CharField(max_length=50, null=False)
    mark = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=False)
    count = models.IntegerField(default=1)
    price = models.FloatField(default=0)
    rubric = models.ForeignKey(Rubric, related_name='products',null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
