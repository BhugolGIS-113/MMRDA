# Generated by Django 4.1.5 on 2023-01-16 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMonitoring', '0041_remove_pap_presentphotograp_papphotographs'),
    ]

    operations = [
        migrations.AddField(
            model_name='pap',
            name='presentPhotograp',
            field=models.ImageField(blank=True, null=True, upload_to='PAP/presentphotograph'),
        ),
        migrations.DeleteModel(
            name='PAPPhotographs',
        ),
    ]