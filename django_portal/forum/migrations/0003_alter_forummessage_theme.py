# Generated by Django 4.1.5 on 2023-02-04 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_alter_forumtheme_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forummessage',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='forum.forumtheme'),
        ),
    ]
