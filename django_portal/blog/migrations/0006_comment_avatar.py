# Generated by Django 4.1 on 2023-01-06 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='avatar',
            field=models.ImageField(null=True, upload_to='upload/'),
        ),
    ]