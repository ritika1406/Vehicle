# Generated by Django 3.2.6 on 2021-10-31 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicledata',
            name='vehiclenumber',
            field=models.CharField(max_length=50),
        ),
    ]