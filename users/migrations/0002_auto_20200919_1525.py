# Generated by Django 3.1.1 on 2020-09-19 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialuser',
            name='first_name',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='socialuser',
            name='last_name',
            field=models.TextField(max_length=30),
        ),
    ]