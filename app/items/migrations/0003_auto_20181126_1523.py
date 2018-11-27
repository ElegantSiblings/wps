# Generated by Django 2.1.3 on 2018-11-26 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='items',
            field=models.ManyToManyField(to='items.Category'),
        ),
    ]
