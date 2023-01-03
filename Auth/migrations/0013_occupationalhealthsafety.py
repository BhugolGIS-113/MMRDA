# Generated by Django 4.1.2 on 2022-11-18 06:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0012_materialsourcing'),
    ]

    operations = [
        migrations.CreateModel(
            name='occupationalHealthSafety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nature_of_accident', models.CharField(max_length=255)),
                ('medical_check', models.BooleanField()),
                ('accidental_check', models.BooleanField()),
                ('incident_issuer', models.BooleanField()),
                ('date_of_incoident', models.DateTimeField(auto_now_add=True)),
                ('barricading', models.BooleanField()),
                ('photographs', models.ImageField(null=True, upload_to='photographs/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
