# Generated by Django 4.2.20 on 2025-03-27 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe_orders', '0002_alter_order_total_price_orderdish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
    ]
