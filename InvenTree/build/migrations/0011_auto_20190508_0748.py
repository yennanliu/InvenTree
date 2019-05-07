# Generated by Django 2.2 on 2019-05-07 21:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0010_auto_20190505_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='status',
            field=models.PositiveIntegerField(choices=[(10, 'Pending'), (20, 'Allocated'), (30, 'Cancelled'), (40, 'Complete')], default=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
