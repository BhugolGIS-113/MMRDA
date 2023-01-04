from django.db import models
from Auth.models import User
from django.contrib.gis.db import models
# Create your models here.


class Baseclass(models.Model):
    choices = [('January-March', 'January-March'), ('April-June','April-June'),
             ('July-September', 'July-September') ,('October-December' ,'October-December')]
    quarter = models.CharField(
        max_length=255, choices=choices, null=True, blank=True)
    package_choice = [('CA-08', 'CA-08'), ('CA-09', 'CA-09'), ('CA-10', 'CA-10'),
                      ('CA-11', 'CA-11'), ('CA-12', 'CA-12'), ('CA-54', 'CA-54')]
    packages= models.CharField(
        max_length=255, choices=package_choice,  null=True, blank=True)
    location = models.PointField(null=True, blank=True)
    dateOfMonitoring = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True


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

# ---------------------Occupational Health & safety Model --------------------
class occupationalHealthSafety(Baseclass):
    location = models.PointField(blank=True)
    JoiningMedicalCheckup= models.BooleanField(null=True, blank=True)
    PPEkit  = models.BooleanField( blank=True)
    TrainingToWorkers = models.BooleanField( blank=True)
    HouseKeeping = models.BooleanField( blank=True)
    PowerSupplySystem = models.BooleanField(blank=True)
    AssemblyArea = models.BooleanField(blank=True)
    AmbulanceArrangement = models.BooleanField(blank=True)
    ToiletFacility = models.BooleanField( blank=True)
    SafeMomentPasage = models.BooleanField(blank=True)
    MaterialKeepingPracticeChoices = [('Safe' , 'Safe'), ('Unsafe' , 'Unsafe'), ('Need Improvements' , 'Need Improvements')]
    MaterialKeepingPractice = models.CharField(max_length= 255 , choices= MaterialKeepingPracticeChoices ,blank = True , null = True)
    accidental_check = models.BooleanField(blank= True)
    SafetyGearStatus = models.BooleanField(blank= True)
    Barricading = models.BooleanField(blank= True)

    NatureOfAccident = models.CharField(max_length=255,blank=True , null = True)
    IncidentTypeChoices = [('Reportable Accident' , 'Reportable Accident'), ('Reportable Non-Fatal Accident' , 'Reportable Non-Fatal Accident'),
                        ('First Aid Cases' , 'First Aid Cases'), ('Dangerous Occurrences' , 'Dangerous Occurrences'),
                        ('Man Days lost' , 'Man Days Lost'), ('Major (Road accident)' , 'Major (Road accident)'),
                        ('Road Incident' , 'Road Incident') , ('Tree Broken' , 'Tree Broken'), ('Natural Death' , 'Natural Death'),
                        ('3rd Party Incident' , 'Third Party Incident')]
    
    TypeOfIncident = models.CharField(max_length=255, choices = IncidentTypeChoices, blank=True , null = True )
    IncidentDetails = models.TextField(max_length= 255 , blank=True , null = True)
    IdentifiedCauseOfIncident = models.CharField(max_length=255, blank = True , null = True )
    Outcome = models.CharField(max_length=255, blank = True , null = True )
    CompensationPaid = models.PositiveIntegerField(blank = True , null = True )
    photographs = models.ImageField(upload_to='OccupationalHealth&Safety/', null=True, blank=True)
    Remarks = models.TextField(max_length=255, blank = True , null = True)





class Contactus(models.Model):
    name = models.CharField(max_length=255 , null = True , blank= True) 
    email = models.EmailField(max_length=255 , verbose_name= 'Email')
    messsage = models.TextField(max_length= 255 , blank= True , null = True )
    