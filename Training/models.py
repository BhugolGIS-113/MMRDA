from django.db import models
from Auth.models import User
from django.contrib.gis.db.models import PointField , LineStringField
from django.contrib.gis.geos import Point, Polygon, LineString
# Create your models here.


class Baseclass(models.Model):
    quarter = models.CharField(max_length=255, null=True, blank=True)
    packages= models.CharField(max_length=255,   null=True, blank=True)
    location = PointField(null=True, blank=True)
    dateOfMonitoring = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True


class traning(Baseclass):
    user = models.ForeignKey(User,related_name='training_User' , on_delete=models.CASCADE)
    category = models.CharField(max_length=255, null=True, blank=True)
    traning_title = models.CharField(max_length=255, null=True, blank=True)
    # location = models.CharField(max_length=255, blank=True, null=True)
    no_of_attends = models.IntegerField(null=True, blank=True)
    male = models.CharField(max_length=255, null=True, blank=True)
    female = models.CharField(max_length=255, null=True, blank=True)
    incharge_person = models.CharField(max_length=253, null=True, blank=True)
    traninig_initiated_by = models.CharField(
        max_length=255, null=True, blank=True)
    conduct_date = models.DateField(auto_now=True, null=True, blank=True)
    traning_date = models.DateField(auto_now=True, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    photographs = models.ImageField(
        upload_to='traning_photographs/', null=True, blank=True)



# #----------------------------- PHOTOGRAPHS MODEL-----------------------------------------

class photographs(models.Model):
    # site_name = models.CharField(max_length=255, null=True, blank=True)
    # incharge_person = models.CharField(max_length=244, null=True, blank=True)
    user = models.ForeignKey(User , related_name= 'photograph_User' , on_delete= models.CASCADE , blank = True) 
    photograph_title = models.CharField(max_length=255, null=True , blank=True)
    photographs_uploaded_by = models.CharField(
        max_length=100, null=True, blank=True)
    location = PointField(null= True, blank=True)
    date = models.DateTimeField( null=True, blank=True)
    site_photographs = models.ImageField(
        upload_to= 'site_photographs/', null=True, blank=True)


# ---------------------Occupational Health & safety Model --------------------
class occupationalHealthSafety(Baseclass):
    user = models.ForeignKey(User, related_name='occupational_health_safety_User' , on_delete= models.CASCADE , blank = True)
    location = PointField(blank=True)
    joiningMedicalCheckup = models.BooleanField(null=True, blank=True)
    ppeKit   = models.BooleanField( blank=True)
    trainingToWorkers  = models.BooleanField( blank=True)
    houseKeeping  = models.BooleanField( blank=True)
    powerSupplySystem  = models.BooleanField(blank=True)
    assemblyArea  = models.BooleanField(blank=True)
    ambulanceArrangement  = models.BooleanField(blank=True)
    toiletFacility  = models.BooleanField( blank=True)
    safeMomentPassage = models.BooleanField(blank=True)

    materialKeepingPractice = models.CharField(max_length= 255 ,blank = True , null = True)
    accidentalCheck = models.BooleanField(blank= True)
    safetyGearStatus = models.BooleanField(blank= True)
    barricading = models.BooleanField(blank= True)

    natureOfAccident  = models.CharField(max_length=255,blank=True , null = True)
    typeOfIncident = models.CharField(max_length=255,  blank=True , null = True )
    incidentDetails = models.TextField(max_length= 255 , blank=True , null = True)
    identifiedCauseOfIncident = models.CharField(max_length=255, blank = True , null = True )
    outcome = models.CharField(max_length=255, blank = True , null = True )
    compensationPaid = models.PositiveIntegerField(blank = True , null = True )
    photographs = models.ImageField(upload_to='OccupationalHealth&Safety/', null=True, blank=True)
    document = models.FileField(blank = True , null = True )
    remarks = models.TextField(max_length=255, blank = True , null = True)



class Contactus(models.Model):
    name = models.CharField(max_length=255 , null = True , blank= True) 
    email = models.EmailField(max_length=255 , verbose_name= 'Email')
    messsage = models.TextField(max_length= 255 , blank= True , null = True )
    location =PointField(blank = True , null = True )
    

class  ContactusImage(models.Model):
    contactus = models.ForeignKey(Contactus, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to = 'contactus/images', max_length= 255 , blank = True , null = True)

    def __str__(self) -> str:
        return self.contactus.location

    