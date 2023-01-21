# Generated by Django 4.1.5 on 2023-01-12 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMonitoring', '0037_rename_genralphotographs_labourcamp_photographs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pap',
            old_name='areaOfLand',
            new_name='areaOfAsset',
        ),
        migrations.RemoveField(
            model_name='pap',
            name='filledBy',
        ),
        migrations.RemoveField(
            model_name='pap',
            name='individualLandAsset',
        ),
    ]