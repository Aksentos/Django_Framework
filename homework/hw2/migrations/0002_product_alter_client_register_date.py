# Generated by Django 5.0.6 on 2024-06-09 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=100)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('product_add_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='register_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
