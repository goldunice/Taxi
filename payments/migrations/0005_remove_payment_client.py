# Generated by Django 5.0.1 on 2024-01-27 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_payment_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='client',
        ),
    ]
