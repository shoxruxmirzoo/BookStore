# Generated by Django 3.0.5 on 2020-04-01 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20200401_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]
