# Generated by Django 4.1.5 on 2023-01-12 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Training', '0010_alter_contactus_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='images',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
    ]
