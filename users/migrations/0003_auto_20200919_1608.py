# Generated by Django 3.1.1 on 2020-09-19 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200919_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialuser',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='socialuser',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
    ]
