# Generated by Django 3.2 on 2022-01-06 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_rating_rating_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='rating_total',
            field=models.IntegerField(default=0),
        ),
    ]
