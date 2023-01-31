from django.db import models
from Auth.models import User
from django.contrib.gis.db.models import PointField, LineStringField
from django.contrib.gis.geos import Point, Polygon, LineString
# Create your models here.


class Baseclass(models.Model):
    quarter = models.CharField(max_length=255, null=True, blank=True)
    packages = models.CharField(max_length=255,   null=True, blank=True)
    location = PointField(null=True, blank=True)
    dateOfMonitoring = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True


class traning(Baseclass):
    user = models.ForeignKey(
        User, related_name='training_User', on_delete=models.CASCADE)
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
    user = models.ForeignKey(
        User, related_name='photograph_User', on_delete=models.CASCADE, blank=True)
    photograph_title = models.CharField(max_length=255, null=True, blank=True)
    photographs_uploaded_by = models.CharField(
        max_length=100, null=True, blank=True)
    location = PointField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    site_photographs = models.ImageField(
        upload_to='site_photographs/', null=True, blank=True)


# ---------------------Occupational Health & safety Model --------------------
class occupationalHealthSafety(Baseclass):
    user = models.ForeignKey(
        User, related_name='occupational_health_safety_User', on_delete=models.CASCADE, blank=True)
    location = PointField(blank=True)
    joiningMedicalCheckup = models.BooleanField(null=True, blank=True)
    ppeKit = models.BooleanField(blank=True)
    trainingToWorkers = models.BooleanField(blank=True)
    houseKeeping = models.BooleanField(blank=True)
    powerSupplySystem = models.BooleanField(blank=True)
    assemblyArea = models.BooleanField(blank=True)
    ambulanceArrangement = models.BooleanField(blank=True)
    toiletFacility = models.BooleanField(blank=True)
    safeMomentPassage = models.BooleanField(blank=True)

    materialKeepingPractice = models.CharField(
        max_length=255, blank=True, null=True)
    accidentalCheck = models.BooleanField(blank=True)
    safetyGearStatus = models.BooleanField(blank=True)
    barricading = models.BooleanField(blank=True)

    natureOfAccident = models.CharField(max_length=255, blank=True, null=True)
    typeOfIncident = models.CharField(max_length=255,  blank=True, null=True)
    incidentDetails = models.TextField(max_length=255, blank=True, null=True)
    identifiedCauseOfIncident = models.CharField(
        max_length=255, blank=True, null=True)
    outcome = models.CharField(max_length=255, blank=True, null=True)
    compensationPaid = models.PositiveIntegerField(blank=True, null=True)
    photographs = models.ImageField(
        upload_to='OccupationalHealth&Safety/', null=True, blank=True)
    document = models.FileField(blank=True, null=True)
    remarks = models.TextField(max_length=255, blank=True, null=True)


class Contactus(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, verbose_name='Email')
    messsage = models.TextField(max_length=255, blank=True, null=True)
    location = PointField(blank=True, null=True)


class ContactusImage(models.Model):
    # contactus = models.ForeignKey(
    #     Contactus, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(
        upload_to='contactus/images', max_length=255, blank=True, null=True)


class PreConstructionStage(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    ShiftingofUtilities = models.BooleanField(default=False)
    RulesOfShiftingofUtilities = models.CharField(max_length=255, default='''High tension power line, water supply pipeline, sewer
                                                                            line, gas pipeline etc. as per MCGM guide lines''')
    ResponsibilityOfShiftingofUtilities = models.CharField(
        max_length=255, blank=True)
    CurrentStatusOfShiftingofUtilities = models.CharField(
        max_length=255, blank=True, null=True)

    PermissionForFellingOfTrees = models.BooleanField(default=False)
    RulesOfPermissionForFellingOfTrees = models.CharField(
        max_length=255, blank=True, null=True)
    ResponsibilityOfPermissionForFellingOfTrees = models.CharField(
        max_length=255, blank=True, null=True)
    CurrentStatusPermissionForFellingOfTrees = models.CharField(
        max_length=255, blank=True, null=True)

    CRZClearance = models.BooleanField(default=False)
    RulesOfCRZClearance = models.CharField(
        max_length=255, default='''As per CRZ Rules, MOEF&CC.''', blank=True, null=True)
    ResponsibilityOfCRZClearance = models.CharField(
        max_length=255, blank=True, null=True)
    CurrentStatusCRZClearance = models.CharField(
        max_length=255, blank=True, null=True)

    ForestClearance = models.BooleanField(default=False)
    RulesOfForestClearance = models.CharField(
        max_length=255, default='''Forest Conservation Act, 1980, amended 1988.''', blank=True, null=True)
    ResponsibilityOfForestClearance = models.CharField(
        max_length=255, blank=True, null=True)
    CurrentStatusOfForestClearance = models.CharField(
        max_length=255, blank=True, null=True)


class ConstructionStage(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE,
                             related_name='user_ConstructionStage', null=True)  # User profile
    ConsenttToEstablishOoperate = models.BooleanField(default=False)
    RulesOfConsenttToEstablishOoperate = models.CharField(
        max_length=255, default='Air (Prevention and Control of Pollution) Act')
    ResponsibilityOfConsenttToEstablishOoperate = models.CharField(
        max_length=255, blank=True, null=True)
    CurrentStatusOfConsenttToEstablishOoperate = models.CharField(
        max_length=255, blank=True, null=True)

    PermissionForSandMiningFromRiverbed = models.BooleanField(default=False)
    RulesOfSandMiningFromRiverbed = models.CharField(
        max_length=255, default='Environment (Protection) Act')
    ResponsibilityOfSandMiningFromRiverbed = models.CharField(
        max_length=255, blank=True, null=True)
    CurrentStatusOfSandMiningFromRiverbed = models.CharField(
        max_length=255, blank=True, null=True)

    PermissionForGroundWaterWithdrawal = models.BooleanField(default=False)
    RulesForGroundWaterWithdrawal = models.CharField(
        max_length=255, default='Environment (Protection) Act')
    ResponsibilityForGroundWaterWithdrawal = models.CharField(
        max_length=255, blank=True, null=True)
    CurrentStatusOfGroundWaterWithdrawal = models.CharField(
        max_length=255, blank=True, null=True)

    AuthorizationForCollectionDisposalManagement = models.BooleanField(
        default=False)
    RulesForCollectionDisposalManagement = models.CharField(
        max_length=255, default='Hazardous waste (Management andHandling) Rules')
    ResponsibilityForCollectionDisposalManagement = models.CharField(
        max_length=255, blank=True, null=True)
    CurrentStatusOfCollectionDisposalManagement = models.CharField(
        max_length=255, blank=True, null=True)

    AuthorizationForSolidWaste = models.BooleanField(default=False)
    RulesForSolidWaste = models.CharField(
        max_length=255, default='Municipal Solid waste Rules')
    ResponsibilityOfSolidWaste = models.CharField(
        max_length=255, blank=True, null=True)
    CurrentStatusOfSolidWaste = models.CharField(
        max_length=255, blank=True, null=True)

    DisposalOfBituminousAndOtherWaste = models.BooleanField(default=False)
    RulesForDisposalOfBituminousAndOtherWaste = models.CharField(
        max_length=255, default='Hazardous waste (Management andHandling) Rules')
    ResponsibilityOfDisposalOfBituminousAndOtherWaste = models.CharField(
        max_length=255, blank=True, null=True)
    CurrentStatusOfDisposalOfBituminousAndOtherWaste = models.CharField(
        max_length=255, blank=True, null=True)

    ConsentToDisposalOfsewagefromLabourCamps = models.BooleanField(
        default=False)
    RulesForDisposalOfsewagefromLabourCamps = models.CharField(
        max_length=255, default='Water (Prevention and Control of Pollution) Act')
    ResponsibilityOfDisposalOfsewagefromLabourCamps = models.CharField(
        max_length=255, blank=True, null=True)
    CurrentStatusOfDisposalOfsewagefromLabourCamps = models.CharField(
        max_length=255, blank=True, null=True)

    PollutionUnderControlCertificate = models.BooleanField(default=False)
    RulesForPollutionUnderControl = models.CharField(
        max_length=255, default='Central Motor and Vehicles Act')
    ResponsibilityOfPollutionUnderControl = models.CharField(
        max_length=255, blank=True, null=True)
    CurrentStatusPollutionUnderControl = models.CharField(
        max_length=255, blank=True, null=True)

    RoofTopRainWaterHarvesting = models.BooleanField(default=False)
    RulesForRoofTopRainWaterHarvesting = models.CharField(
        max_length=255, default='Central Ground Water Authority (CGWA),Guidelines')
    ResponsibilityOfRoofTopRainWaterHarvesting = models.CharField(
        max_length=255, blank=True, null=True)
    CurrentStatusRoofTopRainWaterHarvesting = models.CharField(
        max_length=255, blank=True, null=True)
