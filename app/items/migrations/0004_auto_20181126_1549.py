# Generated by Django 2.1.3 on 2018-11-26 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20181126_1523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='items',
            new_name='categories',
        ),
    ]
