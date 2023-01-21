# Generated by Django 4.1.5 on 2023-01-17 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EnvMonitoring', '0026_treemanagment_cbotonicalname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treemanagment',
            name='Cdocuments',
        ),
        migrations.RemoveField(
            model_name='treemanagment',
            name='Cphotographs',
        ),
        migrations.RemoveField(
            model_name='treemanagment',
            name='Edocuments',
        ),
        migrations.RemoveField(
            model_name='treemanagment',
            name='Ephotographs',
        ),
        migrations.CreateModel(
            name='TreePhotographs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ephotographs', models.ImageField(blank=True, null=True, upload_to='Existingtree_photos/')),
                ('Edocuments', models.FileField(blank=True, null=True, upload_to='existingTree_documents/')),
                ('Cphotographs', models.ImageField(blank=True, null=True, upload_to='newTree_photographs/')),
                ('Cdocuments', models.FileField(blank=True, null=True, upload_to='newTree_documents/')),
                ('Tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TreeManagment', to='EnvMonitoring.treemanagment')),
            ],
        ),
    ]