# Generated by Django 4.1.5 on 2023-08-05 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnvMonitoring', '0035_materialmanegmanet_materialstoragecondition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noise',
            name='noiseLevel',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
