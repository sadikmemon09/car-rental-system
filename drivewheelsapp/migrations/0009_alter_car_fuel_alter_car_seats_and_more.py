# Generated by Django 5.0.6 on 2024-07-12 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivewheelsapp', '0008_car_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fuel',
            field=models.CharField(choices=[('PETROL', 'Petrol'), ('DIESEL', 'Diesel'), ('CNG', 'CNG')], max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='seats',
            field=models.TextField(choices=[('5STR', '5STR'), ('7STR', '7STR')], max_length=30),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('MANUAL', 'Manual'), ('AUTOMATIC', 'Automatic')], max_length=30),
        ),
    ]
