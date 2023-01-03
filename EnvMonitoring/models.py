from django.db import models
from Auth.models import User
from django.db.models.signals import post_save
from django.contrib.gis.db import models
# Create your models here.


# class EnvMonitoring(models.Model):
#     env_monitoring = models.ForeignKey(
#         User, related_name="Quality_Monitoring", on_delete=models.CASCADE , null=True   , blank=True)
#     choices = [('CA-07', 'CA-07'), ('CA-10', 'CA-10'), ('CA-09', 'CA-09')]
#     package = models.CharField(
#         max_length=255, choices=choices, null=True, blank=True)

#     def __str__(self) -> str:
#         return self.env_monitoring.email


# class EnvQualityMonitoring(models.Model):
#     eqm_id = models.OneToOneField(
#         EnvMonitoring, related_name='EnvQualityMonitoring', on_delete=models.CASCADE , null=True   , blank=True)

#     def __str__(self) -> str:
#         return self.eqm_id.env_monitoring.email
# def create_data(sender, instance, **kwargs):
#     if kwargs['created']:
#         created = EnvQualityMonitoring.objects.create(eqm_id=instance)
# post_save.connect(create_data, sender=EnvMonitoring)


# Abstarct Baseclass for EnvMonitoring for common field
class Baseclass(models.Model):
    choices = [('January-March', 'January-March'), ('April-June','April-June'),
             ('July-September', 'July-September') ,('October-December' ,'October-December')]
    quarter = models.CharField(
        max_length=255, choices=choices, null=True, blank=True)
    monthsChoices = [('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'),
                     ('June', 'June'), ('July', 'July'), ('August',
                                                          'August'), ('September', 'September'), ('October', 'October'),
                     ('November', 'November'), ('December', 'December')]
    month = models.CharField(
        max_length=255, choices=monthsChoices, null=True, blank=True)
    package_choice = [('CA-08', 'CA-08'), ('CA-09', 'CA-09'), ('CA-10', 'CA-10'),
                      ('CA-11', 'CA-11'), ('CA-12', 'CA-12'), ('CA-54', 'CA-54')]
    packages = models.CharField(
        max_length=255, choices=package_choice,  null=True, blank=True)
    location = models.PointField(null=True, blank=True)
    dateOfConduct = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True


class Air(Baseclass):
    # air_id = models.ForeignKey( EnvQualityMonitoring, related_name='airs', on_delete=models.CASCADE , null= True   , blank=True)
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
    # water_id = models.ForeignKey(EnvQualityMonitoring, related_name='waters', on_delete=models.CASCADE , null= True   , blank=True)
    qualityOfWater = models.CharField(max_length=255, null=True, blank=True)
    sourceOfWater = models.CharField(max_length=255, null=True, blank=True)
    waterDisposal = models.CharField(max_length=255, null=True, blank=True)


class Noise(Baseclass):
    # noise_id = models.ForeignKey(EnvQualityMonitoring, related_name="noises", on_delete=models.CASCADE , null =True   , blank=True )
    noiseLevel = models.CharField(max_length=255, null=True, blank=True)
    period = [("1 hour", "1 hour"), ("3 hours", "3 hours"),
              ("6 hours", "6 hours"), ]
    monitoringPeriod = models.CharField(
        max_length=255, choices=period, null=True, blank=True)

    # def __str__(self) -> str:
    #     return "filled By :- " + self.noise_id.eqm_id.env_monitoring.email


class TreeManagment(Baseclass):
    
    EtreeID = models.CharField(max_length=255,null = True ,blank = True)
    EcommanName = models.CharField(max_length=255, blank=True, null=True)
    EbotanicalName = models.CharField(max_length=255, null=True, blank=True)
    Econdition = models.CharField(max_length=255, null=True, blank=True)

    actionChoices = [('Transplanted' , 'Transplanted'), ('New Tree Planted' , 'New Tree Planted'),
                     ('No action Taken' , 'No action Taken')]
    actionTaken = models.CharField(max_length=255 , choices = actionChoices,blank=True, null=True)
    noOfTreeCut = models.IntegerField(null=True, blank=True)
    Ephotographs = models.ImageField(
        upload_to="Existingtree_photos/", null=True, blank=True)
    Edocuments = models.FileField(upload_to='existingTree_documents/', null = True , blank=True)
    Eremarks = models.TextField(blank=True, null=True )
    
    Clocation = models.PointField(null = True , blank=True)
    Cname= models.CharField(max_length=255 ,blank=True, null=True )
    CbotonicalName = models.CharField(max_length=255 , blank=True , null= True)
    Ccondition = models.CharField(max_length= 255 ,blank = True , null = True)   
    Cphotographs = models.ImageField(upload_to="newTree_photographs/", null=True, blank=True)
    Cdocuments = models.FileField(upload_to="newTree_documents/", null  = True, blank=True  )
    Cremarks = models.TextField(max_length= 255 , null = True , blank = True)
   


class WasteTreatments(Baseclass):
    # waste_id = models.ForeignKey(
    #     EnvMonitoring, related_name="waste_treatments", on_delete=models.CASCADE, null=True, blank=True)
    _type = [('Hazardous Waste', 'Hazardous'), ('Bio Waste', 'Bio'),
             ('Electrical Waste', 'Electrical'),  ('Non-Bio waste', 'Non-Bio')]
    wastetype = models.CharField(
        max_length=255, choices=_type, null=True, blank=True)
    choices = [('Disposal', 'Disposal'), ('Dumped', 'Dumped'), ('Transportation', 'Transportation'),
               ('Recycling', 'Recycling')]
    quantity = models.IntegerField(null=True, blank=True)
    wastehandling = models.CharField(
        max_length=255, choices=choices, blank=True, null=True)
    wasteHandlingLocation = models.PointField(null=True, blank=True)
    photographs = models.ImageField(upload_to='waste_photographs/' ,null=True, blank=True)
    documents = models.FileField(upload_to='waste_documents' , null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)


class MaterialSourcing(Baseclass):
    # materialsourcing_id = models.ForeignKey(
    #     EnvMonitoring, related_name="MaterialSourcing", on_delete=models.CASCADE, null=True, blank=True)
    typeOfMaterial = models.CharField(max_length=255,  null=True, blank=True)
    quarrySourceChoices = [('Mines', 'Mines'), ('Blast', 'Blast')]
    sourceChoices = [('Quarry', 'Quarry'), ('Factory', 'Factory'), ('Casting Yard',
                                                                    'Casting Yard'), ('Local Vendor', 'Local Vendor'), ('Others', 'Others')]
    source = models.CharField(
        max_length=255, choices=sourceChoices,  null=True, blank=True)
    approvals = models.FileField(null=True, blank=True)
    sourceOfQuarry = models.CharField(
        max_length=255, choices=quarrySourceChoices,  null=True, blank=True)
    photographs = models.ImageField(upload_to='materialsourcing_photographs/',null=True, blank=True)
    documents = models.FileField(upload_to='materialsourcing_documents', null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    # def __str__(self) -> str:
    #     return self.materialsourcing_id.env_monitoring.email
