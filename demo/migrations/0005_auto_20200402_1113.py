# Generated by Django 3.0.5 on 2020-04-02 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_auto_20200401_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn_10', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='number',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='demo.BookNumber'),
        ),
    ]
