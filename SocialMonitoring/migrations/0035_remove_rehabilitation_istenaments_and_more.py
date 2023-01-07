# Generated by Django 4.1.5 on 2023-01-06 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SocialMonitoring', '0034_labourcamp_user_rehabilitation_dateofmonitoring_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rehabilitation',
            name='isTenaments',
        ),
        migrations.AddField(
            model_name='constructionsitedetails',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='constructionsite_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rehabilitation',
            name='typeOfTenaments',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='constructionsitedetails',
            name='availabilityOfDoctorCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='constructionsitedetails',
            name='barricadingCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='constructionsitedetails',
            name='demarkationOfPathwaysCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='constructionsitedetails',
            name='drinkingWaterCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='constructionsitedetails',
            name='firstAidKitCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='constructionsitedetails',
            name='packages',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='constructionsitedetails',
            name='quarter',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='constructionsitedetails',
            name='regularHealthCheckupCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='constructionsitedetails',
            name='signagesLabelingCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='constructionsitedetails',
            name='toiletCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='labourcamp',
            name='availabilityOfDoctorCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='labourcamp',
            name='demarkationOfPathwaysCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='labourcamp',
            name='drinkingWaterCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='labourcamp',
            name='fireExtinguishCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='labourcamp',
            name='firstAidKitCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='labourcamp',
            name='kitchenAreaCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='labourcamp',
            name='modeOfTransportation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='labourcamp',
            name='packages',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='labourcamp',
            name='quarter',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='labourcamp',
            name='regularHealthCheckupCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='labourcamp',
            name='roomsOrDomsCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='labourcamp',
            name='segregationOfwasteCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='labourcamp',
            name='signagesLabelingCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='labourcamp',
            name='toiletCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='labourcamp',
            name='transportationFacilityCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pap',
            name='actionTaken',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pap',
            name='categoryOfPap',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pap',
            name='eligibility',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pap',
            name='legalStatus',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pap',
            name='packages',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pap',
            name='quarter',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pap',
            name='typeOfAsset',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rehabilitation',
            name='compensationStatus',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rehabilitation',
            name='isEngagementType',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rehabilitation',
            name='isRelocationAllowance',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rehabilitation',
            name='livelihoodSupportCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rehabilitation',
            name='packages',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rehabilitation',
            name='quarter',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rehabilitation',
            name='trainingCondition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rehabilitation',
            name='trainingPhotograph',
            field=models.ImageField(blank=True, null=True, upload_to='rehabitation/trainingPhotograph/'),
        ),
        migrations.AlterField(
            model_name='rehabilitation',
            name='typeOfCompensation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
