# Generated by Django 4.2.1 on 2023-05-30 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
