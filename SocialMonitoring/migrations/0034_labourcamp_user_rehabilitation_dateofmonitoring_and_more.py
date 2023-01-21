# Generated by Django 4.1.5 on 2023-01-06 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SocialMonitoring', '0033_pap_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='labourcamp',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='LaboursCamp_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rehabilitation',
            name='dateOfMonitoring',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rehabilitation',
            name='packages',
            field=models.CharField(blank=True, choices=[('CA-08', 'CA-08'), ('CA-09', 'CA-09'), ('CA-10', 'CA-10'), ('CA-11', 'CA-11'), ('CA-12', 'CA-12'), ('CA-54', 'CA-54')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rehabilitation',
            name='quarter',
            field=models.CharField(blank=True, choices=[('January-March', 'January-March'), ('April-June', 'April-June'), ('July-September', 'July-September'), ('October-December', 'October-December')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rehabilitation',
            name='user',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='rehabilitationUser', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]