# Generated by Django 2.1.3 on 2018-12-17 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0008_auto_20181205_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='delivery_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='bill',
            name='total_price',
            field=models.PositiveIntegerField(),
        ),
    ]
