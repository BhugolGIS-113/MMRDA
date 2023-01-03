# Generated by Django 4.1.2 on 2022-12-30 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMonitoring', '0014_rename_isdemarkingofpathways_labourcamp_isdemarkationofpathways_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='constructionsitedetails',
            old_name='dateOfConduct',
            new_name='dateOfMonitoring',
        ),
        migrations.RenameField(
            model_name='labourcamp',
            old_name='dateOfConduct',
            new_name='dateOfMonitoring',
        ),
        migrations.RenameField(
            model_name='pap',
            old_name='dateOfConduct',
            new_name='dateOfMonitoring',
        ),
        migrations.RemoveField(
            model_name='labourcamp',
            name='signagesLabelingCondition',
        ),
    ]
