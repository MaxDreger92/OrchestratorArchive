# Generated by Django 5.0.4 on 2024-06-20 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importing', '0002_remove_fulltablecache_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importercache',
            name='column_label',
            field=models.CharField(blank=True, choices=[('Matter', 'Matter'), ('Property', 'Property'), ('Parameter', 'Parameter'), ('Measurement', 'Measurement'), ('Manufacturing', 'Manufacturing'), ('Metadata', 'Metadata'), ('No label', 'No label'), ('Simulation', 'Simulation'), (None, 'None')], max_length=200, null=True),
        ),
    ]
