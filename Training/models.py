from django.db import models
from Auth.models import User
from django.contrib.gis.db import models
# Create your models here.

class traning(models.Model):
    traning_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, null=True, blank=True)
    traning_title = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    no_of_attends = models.IntegerField(null=True, blank=True)
    male = models.CharField(max_length=255, null=True, blank=True)
    female = models.CharField(max_length=255, null=True, blank=True)
    incharge_person = models.CharField(max_length=253, null=True, blank=True)
    initiated_by = [('GC (Genral Contractor)', 'GC (Genral Contractor)'),
                    ('Consultant', 'Consultant'), ('MMRDA', 'MMRDA')]
    traninig_initiated_by = models.CharField(
        max_length=255, choices=initiated_by, null=True, blank=True)
    conduct_date = models.DateField(auto_now=True, null=True, blank=True)
    traning_date = models.DateField(auto_now=True, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    photographs = models.ImageField(
        upload_to='traning_photographs/', null=True, blank=True)

    def __str__(self) -> str:
        return self.traning_id.email

# #----------------------------- PHOTOGRAPHS MODEL-----------------------------------------

class photographs(models.Model):
    # site_name = models.CharField(max_length=255, null=True, blank=True)
    # incharge_person = models.CharField(max_length=244, null=True, blank=True)
    photograph_title = models.CharField(max_length=255, null=True , blank=True)
    photographs_uploaded_by = models.CharField(
        max_length=100, null=True, blank=True)
    location = models.PointField(null= True, blank=True)
    date = models.DateTimeField( null=True, blank=True)
    site_photographs = models.ImageField(
        upload_to= 'site_photographs/', null=True, blank=True)


class Contactus(models.Model):
    name = models.CharField(max_length=255 , null = True , blank= True) 
    email = models.EmailField(max_length=255 , verbose_name= 'Email')
    messsage = models.TextField(max_length= 255 , blank= True , null = True )
    