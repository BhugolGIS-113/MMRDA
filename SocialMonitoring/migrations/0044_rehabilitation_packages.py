# Generated by Django 4.1.5 on 2023-01-18 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMonitoring', '0043_remove_rehabilitation_packages'),
    ]

    operations = [
        migrations.AddField(
            model_name='rehabilitation',
            name='packages',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]