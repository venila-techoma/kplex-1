# Generated by Django 5.1.4 on 2024-12-12 11:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_booking_created_at_booking_status_booking_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='booking_type',
            field=models.CharField(choices=[('DAILY', 'Date Range'), ('MONTHLY', 'Monthly'), ('YEARLY', 'Yearly')], default='DAILY', max_length=10),
        ),
        migrations.AddField(
            model_name='quotation',
            name='remarks',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quotation',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Cancelled', 'Cancelled'), ('Convert', 'Convert')], default='Pending', max_length=10),
        ),
    ]
