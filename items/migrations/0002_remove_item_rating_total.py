# Generated by Django 3.2 on 2022-01-06 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='rating_total',
        ),
    ]