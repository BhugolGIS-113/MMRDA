# Generated by Django 4.1.5 on 2023-01-04 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMonitoring', '0028_alter_constructionsitedetails_istoilet'),
    ]

    operations = [
        migrations.CreateModel(
            name='labourcampDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LabourCampName', models.CharField(blank=True, max_length=255, null=True)),
                ('LabourCampID', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='rehabilitation',
            name='tenamentsCondition',
        ),
        migrations.RemoveField(
            model_name='rehabilitation',
            name='tenamentsRemarks',
        ),
        migrations.AddField(
            model_name='constructionsitedetails',
            name='barricadingCondition',
            field=models.CharField(blank=True, choices=[('Organized', 'Organized'), ('Not Organized', 'Not Organized'), ('inadequate Organized', 'inadequate Organized')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='constructionsitedetails',
            name='barricadingPhotograph',
            field=models.ImageField(blank=True, null=True, upload_to='constructionSite/barricading_photograph/'),
        ),
        migrations.AddField(
            model_name='constructionsitedetails',
            name='barricadingRemarks',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='constructionsitedetails',
            name='isbarricading',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pap',
            name='areaOfLand',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rehabilitation',
            name='areaOfTenament',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rehabilitation',
            name='livelihoodSupportAmount',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='constructionsitedetails',
            name='constructionSiteID',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='constructionsitedetails',
            name='constructionSiteName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='labourcamp',
            name='LabourCampID',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='labourcamp',
            name='labourCampName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rehabilitation',
            name='isEngagementType',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rehabilitation',
            name='isRelocationAllowance',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rehabilitation',
            name='isTenaments',
            field=models.CharField(blank=True, choices=[('enaments', 'enaments'), ('House', 'House'), ('Flat', 'Flat'), ('Institution', 'Institution'), ('Other', 'Other')], max_length=255),
        ),
    ]