# Generated by Django 4.1.5 on 2023-01-27 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMonitoring', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='constructionsitedetails',
            old_name='constructionSiteID',
            new_name='constructionSiteId',
        ),
    ]
