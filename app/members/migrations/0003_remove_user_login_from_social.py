# Generated by Django 2.1.3 on 2018-11-30 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_user_login_from_social'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='login_from_social',
        ),
    ]
