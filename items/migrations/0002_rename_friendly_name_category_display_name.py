# Generated by Django 3.2 on 2021-12-20 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='friendly_name',
            new_name='display_name',
        ),
    ]
