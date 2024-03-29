# Generated by Django 4.1.5 on 2024-01-24 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnvMonitoring', '0042_air_co'),
    ]

    operations = [
        migrations.AddField(
            model_name='noise',
            name='monitoringPeriod_day',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='noise',
            name='monitoringPeriod_night',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='noise',
            name='noiseLevel_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='noise',
            name='noiseLevel_night',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
