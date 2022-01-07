# Generated by Django 3.2 on 2022-01-06 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=40)),
                ('stripe_payment_id', models.CharField(default='', max_length=250)),
                ('full_name', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order_cost', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('email', models.EmailField(max_length=250)),
                ('telephone', models.CharField(max_length=18)),
                ('address_line1', models.CharField(max_length=100)),
                ('address_line2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(max_length=50)),
                ('county', models.CharField(blank=True, max_length=100, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('postcode', models.CharField(max_length=15)),
                ('customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_size', models.CharField(max_length=3)),
                ('item_cost', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('quantity', models.IntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='checkout.order')),
            ],
        ),
    ]
