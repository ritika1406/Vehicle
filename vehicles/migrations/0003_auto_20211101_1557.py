# Generated by Django 3.2.6 on 2021-11-01 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_alter_vehicledata_vehiclenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicledata',
            name='id',
        ),
        migrations.AlterField(
            model_name='vehicledata',
            name='vehiclenumber',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
