# Generated by Django 4.1.5 on 2023-01-05 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMonitoring', '0030_remove_labourcampdetails_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pap',
            name='governmentLand',
        ),
        migrations.RemoveField(
            model_name='pap',
            name='privateLand',
        ),
    ]
