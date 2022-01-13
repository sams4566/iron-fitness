# Generated by Django 3.2 on 2022-01-13 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('display_name', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('bio', models.TextField()),
                ('sku', models.CharField(blank=True, max_length=250, null=True)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('rating_total', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.category')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_review', to='items.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_star', models.IntegerField(blank=True, null=True)),
                ('two_stars', models.IntegerField(blank=True, null=True)),
                ('three_stars', models.IntegerField(blank=True, null=True)),
                ('four_stars', models.IntegerField(blank=True, null=True)),
                ('five_stars', models.IntegerField(blank=True, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_rating', to='items.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
