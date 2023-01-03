# Generated by Django 4.1.2 on 2022-12-23 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMonitoring', '0010_remove_constructionsitedetails_sitephotographs'),
    ]

    operations = [
        migrations.AddField(
            model_name='labourcamp',
            name='sourceOfWater',
            field=models.CharField(blank=True, choices=[('Tap Water', 'Tap Water'), ('Tanker Water', 'Tanker Water')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='labourcamp',
            name='waterDisposal',
            field=models.CharField(blank=True, choices=[('Nearby', 'Nearby'), ('Civil drain', 'Civil drain'), ('Open drain', 'Open drain')], max_length=255, null=True),
        ),
    ]
