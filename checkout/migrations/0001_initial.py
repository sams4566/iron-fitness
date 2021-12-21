# Generated by Django 3.2 on 2021-12-21 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0002_rename_friendly_name_category_display_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=40)),
                ('customer_name', models.CharField(max_length=55)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order_cost', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('email', models.EmailField(max_length=250)),
                ('telephone', models.CharField(max_length=18)),
                ('address_line1', models.CharField(max_length=100)),
                ('address_line2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(max_length=50)),
                ('county', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(max_length=50)),
                ('postcode', models.CharField(max_length=15)),
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