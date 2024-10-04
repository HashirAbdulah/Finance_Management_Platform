# Generated by Django 5.1.1 on 2024-10-04 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_paymenthistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenthistory',
            name='payment_type',
            field=models.CharField(choices=[('monthly', 'Monthly'), ('hourly', 'Hourly')], max_length=20),
        ),
    ]