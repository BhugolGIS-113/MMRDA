# Generated by Django 4.1.5 on 2023-01-06 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0038_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_RNR',
            field=models.BooleanField(default=False),
        ),
    ]
