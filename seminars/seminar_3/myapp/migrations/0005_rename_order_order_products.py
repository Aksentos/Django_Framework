# Generated by Django 5.0.6 on 2024-06-12 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_order_total_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order',
            new_name='products',
        ),
    ]