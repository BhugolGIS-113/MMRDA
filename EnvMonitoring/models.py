from django.db import models
from Auth.models import User
from django.db.models.signals import post_save
from django.contrib.gis.db import models
# Create your models here.


# Abstarct Baseclass for EnvMonitoring for common field
class Baseclass(models.Model):
    quarter = models.CharField(max_length=255,  null=True, blank=True)
    month = models.CharField(max_length=255, null=True, blank=True)
    packages = models.CharField(max_length=255, null=True, blank=True)
    location = models.PointField(null=True, blank=True)
    dateOfMonitoring = models.DateField(null=True, blank=True)
    class Meta:
        abstract = True

class Air(Baseclass):
    user = models.ForeignKey( User, related_name='airs_user', on_delete=models.CASCADE , null= True   , blank=True)
    PM10 = models.FloatField(blank= True , default= 0, null= True)
    standardPM10 = models.FloatField(blank= True , default=100.00 , null= True)
    SO2 = models.FloatField(blank= True , default= 0, null= True)
    standardSO2 = models.FloatField(blank= True , default = 80.00 , null= True)
    O3 = models.FloatField(blank= True , default= 0, null= True)
    standardO3 = models.FloatField(blank= True , default = 100.00 , null= True)
    NOx = models.FloatField(blank= True , default= 0, null = True)
    standardNOx = models.FloatField(blank= True , default = 80.00 , null= True)
    AQI = models.FloatField(blank= True , default= 0, null = True) 
    Remarks = models.TextField ( blank = True, max_length  = 100, null = True )

class water(Baseclass):
    user = models.ForeignKey(User, related_name='waters', on_delete=models.CASCADE , null= True   , blank=True)
    qualityOfWater = models.CharField(max_length=255, null=True, blank=True)
    sourceOfWater = models.CharField(max_length=255, null=True, blank=True)
    waterDisposal = models.CharField(max_length=255, null=True, blank=True)


class Noise(Baseclass):
    user = models.ForeignKey(User, related_name="noises", on_delete=models.CASCADE , blank=True )
    noiseLevel = models.CharField(max_length=255, null=True, blank=True)
    monitoringPeriod = models.CharField(
        max_length=255, null=True, blank=True)

    # def __str__(self) -> str:
    #     return "filled By :- " + self.noise_id.eqm_id.env_monitoring.email


class TreeManagment(Baseclass):
    user = models.ForeignKey( User ,  related_name="Tree_user" , on_delete= models.CASCADE , blank = True)
    EtreeID = models.CharField(max_length=255,null = True ,blank = True)
    EcommanName = models.CharField(max_length=255, blank=True, null=True)
    EbotanicalName = models.CharField(max_length=255, null=True, blank=True)
    Econdition = models.CharField(max_length=255, null=True, blank=True)

    actionTaken = models.CharField(max_length=255 ,blank=True, null=True)
    noOfTreeCut = models.IntegerField(null=True, blank=True)
    Ephotographs = models.ImageField(upload_to="Existingtree_photos/", null=True, blank=True)
    Edocuments = models.FileField(upload_to='existingTree_documents/', null = True , blank=True)
    Eremarks = models.TextField(blank=True, null=True )
    
    # Clocation = models.PointField(null = True , blank=True)
    # Cname= models.CharField(max_length=255 ,blank=True, null=True )
    # CbotonicalName = models.CharField(max_length=255 , blank=True , null= True)
    # Ccondition = models.CharField(max_length= 255 ,blank = True , null = True)   
    # Cphotographs = models.ImageField(upload_to="newTree_photographs/", null=True, blank=True)
    # Cdocuments = models.FileField(upload_to="newTree_documents/", null  = True, blank=True  )
    # Cremarks = models.TextField(max_length= 255 , null = True , blank = True)
   


class WasteTreatments(Baseclass):
    user = models.ForeignKey(
        User, related_name="waste_treatments", on_delete=models.CASCADE, blank=True)
    wastetype = models.CharField(
        max_length=255,  null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    wastehandling = models.CharField(
        max_length=255, blank=True, null=True)
    wasteHandlingLocation = models.PointField(null=True, blank=True)
    photographs = models.ImageField(upload_to='waste_photographs/' ,null=True, blank=True)
    documents = models.FileField(upload_to='waste_documents' , null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)


class MaterialManegmanet(Baseclass):
    user = models.ForeignKey(User, related_name="MaterialSourcing", on_delete=models.CASCADE, blank=True)
    typeOfMaterial = models.CharField(max_length=255,  null=True, blank=True)
    source = models.CharField(max_length=255,  null=True, blank=True)
    sourceOfQuarry = models.CharField(max_length=255,  null=True, blank=True)
    storageLocation = models.PointField(blank = True , null = True)

    materialStorageType = models.CharField(max_length=255 , blank = True , null = True)
    materialstorageCondition = models.CharField(max_length = 255 , blank = True , null = True)
    materialstoragePhotograph = models.ImageField(upload_to = 'MaterialManegment/materailStorage_Photograph' , blank = True , null = True)

    approvals = models.FileField(null=True, blank=True)
    
    photographs = models.ImageField(upload_to='MaterialManegment/materialsourcing_photographs/',null=True, blank=True)
    documents = models.FileField(upload_to='MaterialManegment/materialsourcing_documents', null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    
    # def __str__(self) -> str:
    #     return self.materialsourcing_id.env_monitoring.email
