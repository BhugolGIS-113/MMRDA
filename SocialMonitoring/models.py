from django.db import models
from Auth.models import User
from django.db.models.signals import post_save
from django.contrib.gis.db import models
from django.utils import timezone
# Create your models here.

# ----------------------------------SOCIAL MONITORING MODLES----------------------------------------

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




class PAP(Baseclass):
    # pap_id = models.ForeignKey(
    #     social_Monitoring, related_name='PAPs', on_delete=models.CASCADE)
    PAPID = models.CharField(max_length=255, blank= True  , null= True)
    nameOfPAP= models.CharField(max_length = 255, blank=True , null= True)
    addressLine1= models.TextField(max_length=255 , blank=True, null= True)
    streetName = models.CharField(max_length=255 , blank=True, null= True)
    pincode = models.PositiveIntegerField(blank= True , null = True)
    dateOfIdentification = models.DateField(blank= True , null = True )
    _eligibilityChoices = [('Eligible', 'eligible'), ('Not eligible', 'Not eligible'),('Pending', 'Pending')]
    eligibility = models.CharField(max_length= 255 ,choices= _eligibilityChoices,  null= True , blank=True)      
    type_of_pap = [
        ('Individual / Joint Holding', 'Individual / Joint Holding'), ('Commercial', 'Commercial'),
        ('Private Land', 'Private Land'),('Government Land' , 'Government Land'), ('Institutional', 'Institutional'),
        ('Other', 'Other')]
    categoryOfPap = models.CharField(max_length=255, choices=type_of_pap, null=True, blank=True)
    privateLand = models.FloatField(blank=True , null = True)
    GovernmentLand = models.FloatField(blank = True , null = True)
    Ownership_status_choices = [('Flat/House', 'Flat/House'), ('Land', 'Land'),('Independent House/Hutment',
                                 'Independent House/Hutment'), ('Other', 'Other')]
    individualLandAsset = models.PositiveIntegerField( blank= True , null = True )
    typeOfAsset = models.CharField(max_length=255, choices=Ownership_status_choices, null=True, blank=True)
    status = [
        ('legal', 'legal'),
        ('illegal', 'illegal'),
        ('under dispute', 'under dispute')]
    legalStatus = models.CharField(max_length=255, choices=status, null=True, blank=True)
    legalDocuments = models.FileField(upload_to='PAP/PAP_legalDocuments/',blank= True , null = True)
    actions = [('Agreed for rehabilitation', 'Agreed for rehabilitation'),
               ('Agreed For compensation', 'Agreed For compensation'),
               ('Not agreed', 'Not agreed')]
    actionTaken = models.CharField(max_length=100, choices=actions, null=True, blank=True)
    notAgreedReason = models.TextField(max_length= 255 , blank = True , null = True )
    presentPhotograp = models.ImageField(upload_to= 'PAP/presentphotograph' , blank = True , null = True)
    remarks = models.TextField(max_length= 255 , blank = True , null = True )
    


class Rehabilitation(models.Model):
    
    location = models.PointField(null=True, blank=True)
    PAPID = models.ForeignKey( PAP, related_name='rehabilitation', on_delete= models.CASCADE)
    dateOfRehabilitation = models.DateField(blank= True, null=True)
    PAPName = models.CharField(max_length=255 , blank = True , null = True)
    
    CompensationStatusChoises = [('Cash Compensation' , 'Cash Compensation'),('Land Provided Assets' , 'Land Provided Assets') ,
                                ('Alternate accommodation' , 'Alternate accommodation'),
                                ('Commercial Unit' , 'Commercial Unit')]
    cashCompensation = models.PositiveIntegerField(blank = True , null = True)
    compensationStatus = models.CharField(max_length=255, choices=CompensationStatusChoises,null=True, blank=True )
    typeOfCompensationChoices = [('2.5 x Area', '2.5 x Area') ,('Cash', 'Cash'),('Both', 'Both'),('Other', 'Other')]
    typeOfCompensation = models.CharField(max_length=255 , choices= typeOfCompensationChoices,null=True, blank= True)
    otherCompensationType = models.CharField(max_length=255, null=True, blank= True)
    
    addressLine1 = models.TextField(max_length=255, blank = True, null = True)
    streetName = models.CharField(max_length=255, blank = True, null = True)
    pincode = models.BigIntegerField(blank = True , null = True)
    
    choices = [('Good' , 'Good'), ('Average' , 'Average'), ('Poor' , 'Poor')]
    
    isShiftingAllowance = models.BooleanField(blank =True)
    shiftingAllowanceAmount = models.PositiveIntegerField(blank = True , null = True  )

    isLivelihoodSupport = models.BooleanField(blank= True)
    livelihoodSupportCondition = models.CharField(max_length=255, choices= choices, blank = True, null = True )
    livelihoodSupportPhotograph = models.ImageField(upload_to='rehabitation/livelihoodSupportPhotograph/' , blank = True , null = True)
    livelihoodSupportRemarks = models.TextField(max_length=255, blank = True , null = True )

    isTraining = models.BooleanField(blank= True )
    trainingCondition = models.CharField(max_length=255, choices= choices, blank = True , null = True )
    trainingPhotograph = models.ImageField('rehabitation/trainingPhotograph/', blank = True , null = True)
    trainingRemarks = models.TextField(max_length=255, blank = True, null = True )

    isTenaments = models.BooleanField(blank =True)
    tenamentsCondition = models.CharField(max_length=255, choices= choices,blank = True , null = True )
    tenamentsPhotograph = models.ImageField(upload_to='rehabitation/tenamentsPhotograph/', blank =True , null = True )
    tenamentsRemarks = models.TextField(max_length=255, blank = True , null = True )

    isRelocationAllowance = models.BooleanField(blank =True , null = True )
    RelocationAllowanceAmount = models.PositiveIntegerField(blank = True , null = True )

    isfinancialSupport = models.BooleanField(blank =True , null = True)
    financialSupportAmount = models.PositiveIntegerField(blank = True ,null = True)

    isCommunityEngagement = models.BooleanField(blank =True , null = True)
    isEngagementType = models.CharField( max_length=255, blank=True , null = True)

    photographs = models.ImageField( upload_to='rehabitation/Rehabitationphotographs/', blank=True, null=True)
    documents = models.FileField(upload_to= 'rehabitation/documents', blank=True, null=True)
    remarks = models.TextField(max_length=255, blank=True , null=True)





# Labour  Camp Model ----------------------------------------------

class LabourCamp(Baseclass):
    YesNoChoices = [('Yes', 'Yes') , ('No', 'No')]
    notRequiredchoices = [('Yes', 'Yes'), ('No', 'No'),('Not Required', 'Not Required')]
    labourcampIdChoices = [('KT-01' , 'KT-01') , ('BY-02' , 'BY-02') , ('BPY-03' , 'BPY-03') , ('KC-04' , 'KC-04'),('GT-05' , 'GT-05')]
    LabourCampID = models.CharField(max_length= 255 , choices= labourcampIdChoices , null= True , blank=True)
    labourCampChoices = [('Kolshet Thane' , 'Kolshet Thane'),('BKC Yard' , 'BKC Yard') , ('Bhakti Park Yard' , 'Bhakti Park Yard') ,
                        ('Kavsar Casting' , 'Kavsar Casting') , ('Gaimukh Thane' , 'Gaimukh Thane')]
    labourCampName = models.CharField(max_length=255, choices= labourCampChoices ,  null=True, blank=True)
    
    choices = [('Good' , 'Good'), ('Average' , 'Average'), ('Poor' , 'Poor')]
    isToilet = models.BooleanField( max_length= 255 ,blank =True)
    toiletCondition = models.CharField(max_length=255,choices=choices, blank = True , null = True )
    toiletPhotograph = models.ImageField(upload_to='Labour Camp/toilet_photographs/' , blank= True , null = True )
    toiletRemarks = models.TextField(max_length= 255 , null = True , blank = True )
    
    isDrinkingWater = models.BooleanField(blank =True)
    drinkingWaterCondition = models.CharField(max_length=255, blank = True , choices= choices , null = True )
    drinkingWaterPhotographs = models.ImageField(upload_to='Labour Camp/drinkingWater_photographs/' , null = True , blank = True )
    drinkingWaterRemarks = models.TextField(max_length=255 , null = True , blank = True )
    # _sourecType = [('Tap Water', 'Tap Water') , ('Tanker Water', 'Tanker Water')]
    # sourceOfWater = models.CharField(max_length= 255, choices= _sourecType, blank = True   , null = True)
    # DisposalChoices = [('Nearby' , 'Nearby') , ('Civil drain' , 'Civil drain') , ('Open drain' , 'Open drain')]
    # waterDisposal = models.CharField(max_length= 255, choices=DisposalChoices, blank = True , null = True) 
    isDemarkationOfPathways = models.BooleanField(blank =True)
    demarkationOfPathwaysCondition = models.CharField(max_length= 255, blank= True , null= True)
    demarkationOfPathwaysPhotographs = models.ImageField(upload_to = 'Labour Camp/demarkingPathways_photographs/' ,  blank= True , null = True )
    demarkationOfPathwaysRemark = models.TextField(max_length=255 , blank = True , null = True)
    # DemarkationOfPathwaysCondition = models.CharField(max_length= 255, choices=YesNoChoices , blank = True , null = True)
    isSignagesLabeling = models.BooleanField(blank =True)
    signagesLabelingCondition = models.CharField(max_length= 255, choices=YesNoChoices ,blank = True , null = True) 
    signagesLabelingPhotographs = models.ImageField(upload_to='Labour Camp/signagesLabeling_Photographs/' ,  blank= True , null = True)
    signagesLabelingRemarks = models.TextField(max_length= 255 ,  blank= True , null = True)
    
    isKitchenArea = models.BooleanField(blank =True , null = True)
    kitchenAreaCondition = models.CharField(max_length= 255, choices=choices , blank = True , null = True)
    kitchenAreaPhotographs = models.ImageField(upload_to='Labour Camp/KitchenArea _photographs/' , blank= True , null = True)
    kitchenAreaRemarks = models.TextField(max_length= 255,  blank= True , null = True)

    isFireExtinguish= models.BooleanField(blank =True , null = True)
    fireExtinguishCondition = models.CharField(max_length= 255, choices=choices, blank = True , null = True )
    fireExtinguishPhotographs = models.ImageField(upload_to='Labour Camp/fireExtinguish_photographs/' ,   blank= True , null = True )
    fireExtinguishRemarks = models.TextField(max_length= 255, blank= True , null = True)

    isRoomsOrDoms = models.BooleanField(blank=True , null = True)
    roomsOrDomsChoices = [('Individual' ,'Individual'), ('Shared Rooms' , 'Shared Rooms')]
    roomsOrDomsCondition = models.CharField(max_length=255 ,  blank= True , null = True, choices = roomsOrDomsChoices)
    roomsOrDomsPhotographs = models.ImageField(upload_to='Labour Camp/rooms_photographs/' , blank = True , null = True )
    roomsOrDomsRemarks = models.TextField(max_length= 255,  blank= True , null = True)

    isSegregationOfWaste = models.BooleanField(blank =True)
    segregationOfwasteCondition = models.CharField(max_length=255 , choices= YesNoChoices , blank= True , null = True)
    segregationOfwastePhotographs = models.ImageField(upload_to = 'labour Camp/segrigationOfWaste_Photographs/' , blank = True , null = True )
    segregationOfwasteRemarks = models.TextField(max_length= 255,  blank= True , null = True )
    
    isRegularHealthCheckup = models.BooleanField(blank= True )
    regularHealthCheckupCondition = models.CharField(max_length= 255, choices=choices,  blank= True , null = True)
    regularHealthCheckupPhotographs = models.ImageField(upload_to='Labour Camp/RegularHealthCheckup_Photographs/' , blank= True , null = True )
    regularHealthCheckupRemarks = models.TextField(max_length= 255,  blank= True , null = True )

    isAvailabilityOfDoctor = models.BooleanField(blank =True)
    availabilityOfDoctorCondition = models.CharField(max_length= 255, choices=choices , blank= True , null = True)
    availabilityOfDoctorPhotographs = models.ImageField(upload_to= 'Labour Camp/AvailabilityOfDoctor_photographs/' ,  blank= True , null = True)
    availabilityOfDoctorRemarks = models.TextField(max_length= 255,  blank= True , null = True )

    isFirstAidKit = models.BooleanField( blank =True)
    firstAidKitCondition = models.CharField(max_length= 255, choices=choices , blank= True , null = True)
    firstAidKitPhotographs = models.ImageField(upload_to='Labour Camp/FirstAidKit_photographs/' , blank= True , null = True)
    firstAidKitRemarks = models.TextField(max_length= 255,  blank= True , null = True )

    transportationFacility = models.BooleanField(blank=True, null = True)
    transportationFacilityCondition = models.CharField(max_length=255,choices = notRequiredchoices ,blank=True, null = True)
    choices = [('Arranged By Contractor', 'Arranged By Contractor'), ('Arranged By MMRDA', 'Arranged By MMRDA')]
    modeOfTransportation = models.CharField(max_length= 255 ,choices= choices, blank=True , null = True)
    distanceFromSite= models.PositiveIntegerField(blank=True , null = True)
    
    GenralPhotographs = models.ImageField( upload_to='Labour Camp/GenralPhotographs/', blank=True, null=True)
    documents = models.FileField(upload_to= 'labourcamp_documents/', blank=True, null=True)
    remarks = models.TextField(max_length=255, blank=True , null=True)


class ConstructionSiteDetails(Baseclass):
    
    # labourCamp_id = models.ForeignKey(
    #     LabourCamp, related_name='constructioncamp', on_delete=models.CASCADE)
    # # quarter =None
    # sitephotographs = models.ImageField(upload_to='site_photographs/' , null=True, blank=True)
    constructionsSiteChoices = [('Kolshet Thane' , 'Kolshet Thane'),('BKC Yard' , 'BKC Yard') , ('Bhakti Park Yard' , 'Bhakti Park Yard') ,
                        ('Kavsar Casting' , 'Kavsar Casting') , ('Gaimukh Thane' , 'Gaimukh Thane')]
    constructionSiteName = models.CharField(max_length=255, choices = constructionsSiteChoices ,   blank=True , null = True )
    constructionSiteIDChoices = [('KT-01' , 'KT-01') , ('BY-02' , 'BY-02') , ('BPY-03' , 'BPY-03') , ('KC-04' , 'KC-04'),('GT-05' , 'GT-05')]
    constructionSiteID = models.CharField(max_length=255, choices = constructionSiteIDChoices ,  blank= True , null = True)
    
    isDemarkingOfPathwaysCheck = models.BooleanField(blank = True)
    isSignagesLabelingCheck = models.BooleanField(blank= True )
    isRegularHealthCheckup = models.BooleanField(default=False)
    isAvailabilityOfDoctor = models.BooleanField(default=False)
    isFirstAidKit = models.BooleanField(default=False)
    isDrinkingWaterCheck  = models.BooleanField(blank =True)
    isToiletFacility = models.BooleanField( blank =True)
    photographs = models.ImageField( upload_to='constructionsite_photographs/', blank=True, null=True)
    documents = models.FileField(upload_to= 'constructionsite_documents/', blank=True, null=True)
    remarks = models.TextField(max_length=255, blank=True , null=True)

