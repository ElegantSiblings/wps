# Generated by Django 2.1.3 on 2018-11-30 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0011_item_ga_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='ga_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
