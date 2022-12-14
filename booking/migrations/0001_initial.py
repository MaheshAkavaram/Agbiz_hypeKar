# Generated by Django 3.2.15 on 2022-09-29 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('customer_name', models.CharField(max_length=60)),
                ('customer_address', models.CharField(max_length=60)),
                ('service_address', models.CharField(max_length=60)),
                ('brand', models.CharField(max_length=60)),
                ('model', models.CharField(max_length=20)),
                ('service_type', models.CharField(max_length=60)),
                ('time_slot', models.CharField(max_length=60)),
                ('date', models.DateField()),
            ],
        ),
    ]
