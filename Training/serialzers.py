
from rest_framework import serializers
from .models import *
from rest_framework_gis.serializers import GeoFeatureModelSerializer
class TraningSerializer(serializers.ModelSerializer):
    longitude=serializers.CharField(max_length=10,required=True)
    latitude=serializers.CharField(max_length=10,required=True)
    class Meta:
        model = traning
        fields =( 'quarter' , 'packages' , 'dateOfMonitoring' ,'category' , 'traning_title' , 'no_of_attends' , 'male' , 'female' ,
                 'longitude' , 'latitude' ,'incharge_person' , 'traninig_initiated_by' , 
                 'conduct_date' , 'traning_date' , 'description' , 'photographs')

    def create(self,data):  
        data.pop('longitude')
        data.pop('latitude')
        return traning.objects.create(**data)


class photographsSerializer(serializers.ModelSerializer):
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    class Meta:
        model = photographs
        fields = ['photograph_title', 'photographs_uploaded_by' , 'longitude' , 'latitude',
                   'date' , 'site_photographs'  ]

    def create(self,data):
        data.pop('latitude')
        data.pop('longitude')
        return photographs.objects.create(**data)

class photographsViewSerializer(serializers.ModelSerializer):
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    class Meta:
        model = photographs
        fields =['id','photograph_title', 'photographs_uploaded_by' , 'longitude' , 'latitude',
                   'date' , 'site_photographs'  ]


class occupationalHealthSafetySerialziers(serializers.ModelSerializer):
    longitude = serializers.CharField(max_length= 255 , required = False) # longitude
    latitude = serializers.CharField(max_length= 255, required = False) # latitude
    class Meta:
        model = occupationalHealthSafety
        fields = ['dateOfMonitoring' ,'packages', 'quarter','longitude', 'latitude' ,
        'joiningMedicalCheckup' , 'ppeKit' ,'trainingToWorkers','houseKeeping' ,
        'powerSupplySystem' ,'assemblyArea' ,'ambulanceArrangement' ,'toiletFacility',
        'safeMomentPassage' ,'materialKeepingPractice','accidentalCheck','safetyGearStatus',
        'barricading','natureOfAccident' ,'typeOfIncident' ,'incidentDetails' ,
        'identifiedCauseOfIncident' ,'outcome' ,'compensationPaid' ,'photographs' ,'remarks']

    
    def create(self,data):
        data.pop('longitude')
        data.pop('latitude')
        return occupationalHealthSafety.objects.create(**data)

class occupationalHealthSafetyViewSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = occupationalHealthSafety
        fields = '__all__'
        geo_field = 'location'
 
class ContactusImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contactus
        fields = "__all__"

class ContactusSerializezr(serializers.ModelSerializer):
    # images =  ContactusImageSerializers(many=True, read_only=True)
    longitude = serializers.CharField(max_length= 255 , required = False) # longitude
    latitude = serializers.CharField(max_length= 255, required = False) # latitude
    uploaded_images1  = serializers.ListField(child=serializers.ImageField(allow_empty_file=True, use_url=False),write_only=True)
    uploaded_images2 = serializers.ListField(child=serializers.ImageField(allow_empty_file=True, use_url=False),write_only=True)
    class Meta:
        model = Contactus
        fields = ('name','email','messsage' , 'longitude' , 'latitude' , 'uploaded_images1' , 'uploaded_images2')

    def create(self,data):
        data.pop('longitude')
        data.pop('latitude')

        uploaded_images1 = data.pop("uploaded_images1")
        uploaded_images2 = data.pop("uploaded_images2")
        contactus = Contactus.objects.create(**data)

        images = [ContactusImage.objects.create(contactus=contactus, images1=image1, images2=image2) 
                                                for image1, image2 in zip(uploaded_images1, uploaded_images2)]
        return contactus
        
class ContactusViewSerialzier(GeoFeatureModelSerializer):
    class Meta:
        model = Contactus
        fields = '__all__'
        geo_field = 'location'


class PreConstructionStageComplianceSerialzier(serializers.ModelSerializer):
    class Meta:
        model =  PreConstructionStage
        fields = ('ShiftingofUtilities' , 'ResponsibilityOfShiftingofUtilities','CurrentStatusOfShiftingofUtilities',
                    'PermissionForFellingOfTrees', 'ResponsibilityOfPermissionForFellingOfTrees','CurrentStatusPermissionForFellingOfTrees',
                   'CRZClearance','ResponsibilityOfCRZClearance' ,  'CurrentStatusCRZClearance' ,
                   'ForestClearance' , 'ResponsibilityOfForestClearance', 'CurrentStatusOfForestClearance')


class ConstructionStageComplainceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionStage 
        # fields = '__all__'
        exclude = ('RulesOfConsenttToEstablishOoperate', 'RulesOfSandMiningFromRiverbed',
        'RulesForGroundWaterWithdrawal' , 'RulesForCollectionDisposalManagement', 'RulesForSolidWaste',
       'RulesForDisposalOfBituminousAndOtherWaste', 'RulesForDisposalOfsewagefromLabourCamps' , 'RulesForPollutionUnderControl',
       'RulesForRoofTopRainWaterHarvesting','user')



class ContactusImagesSeilizer(serializers.ModelSerializer):
    class Meta:
        model = ContactusImage
        fields = '__all__'