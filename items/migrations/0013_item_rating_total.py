# Generated by Django 3.2 on 2022-01-06 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0012_remove_item_rating_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='rating_total',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]
