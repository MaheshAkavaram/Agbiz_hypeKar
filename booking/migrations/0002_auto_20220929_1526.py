# Generated by Django 3.2.15 on 2022-09-29 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='customer_address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='booking',
            name='model',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='service_address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time_slot',
            field=models.CharField(max_length=100),
        ),
    ]
