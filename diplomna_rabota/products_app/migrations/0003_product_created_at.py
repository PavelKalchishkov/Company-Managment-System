# Generated by Django 5.1.6 on 2025-06-14 15:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0002_remove_product_manufacturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
