# Generated by Django 5.1.6 on 2025-07-07 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0009_company_added_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='supplier_address',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='supplier_dds',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='supplier_eik',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='supplier_email',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='supplier_mol',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='supplier_name',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='supplier_phone_number',
        ),
    ]
