# Generated by Django 5.0.6 on 2024-07-14 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivewheelsapp', '0022_totalrent_delete_bookingcart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totalrent',
            name='dropoffDT',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='totalrent',
            name='pickupDT',
            field=models.DateTimeField(),
        ),
    ]
