# Generated by Django 2.1.3 on 2018-11-28 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='order_yn',
            field=models.BooleanField(default=False),
        ),
    ]
