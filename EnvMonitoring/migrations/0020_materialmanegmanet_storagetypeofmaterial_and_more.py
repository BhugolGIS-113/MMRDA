# Generated by Django 4.1.5 on 2023-01-05 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnvMonitoring', '0019_materialmanegmanet_delete_materialsourcing'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialmanegmanet',
            name='storageTypeOfMaterial',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='materialmanegmanet',
            name='materialstorageCondition',
            field=models.CharField(blank=True, choices=[('Safe', 'Safe'), ('Unsafe', 'Unsafe'), ('Need Improvement', 'Need Improvement')], max_length=255, null=True),
        ),
    ]