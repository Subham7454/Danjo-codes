# Generated by Django 5.1.3 on 2024-11-13 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChaiVriety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='chais/')),
                ('date_aded', models.DateTimeField(default=datetime.datetime(2024, 11, 13, 13, 16, 15, 740098, tzinfo=datetime.timezone.utc))),
                ('type', models.CharField(choices=[('ML', 'MASALA'), ('GR', 'GINGER'), ('KL', 'KIWI'), ('PL', 'PALIN'), ('EL', 'ELAICHI')], max_length=2)),
            ],
        ),
    ]
