# Generated by Django 4.2.12 on 2024-05-08 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0048_build_project_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='builditem',
            name='build_line',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allocations', to='build.buildline'),
        ),
    ]
