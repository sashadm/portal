# Generated by Django 4.1 on 2022-09-24 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogentry',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]