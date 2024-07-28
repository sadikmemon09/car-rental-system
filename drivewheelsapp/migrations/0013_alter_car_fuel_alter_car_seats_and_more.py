# Generated by Django 5.0.6 on 2024-07-12 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivewheelsapp', '0012_alter_car_fuel_alter_car_seats_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fuel',
            field=models.IntegerField(choices=[(1, 'Petrol'), (2, 'Diesel'), (3, 'CNG')]),
        ),
        migrations.AlterField(
            model_name='car',
            name='seats',
            field=models.IntegerField(choices=[(1, '5STR'), (2, '7STR')]),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.IntegerField(choices=[(1, 'Manual'), (2, 'Automatic')]),
        ),
    ]
