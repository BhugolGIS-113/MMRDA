
from rest_framework import serializers
from .models import *
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class TraningSerializer(serializers.ModelSerializer):
    class Meta:
        model = traning
        fields = '__all__'


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
 

class ContactusSerializezr(serializers.ModelSerializer):
    longitude = serializers.CharField(max_length= 255 , required = False) # longitude
    latitude = serializers.CharField(max_length= 255, required = False) # latitude
    class Meta:
        model = Contactus
        fields = ('name','email','messsage' , 'longitude' , 'latitude')

    def create(self,data):
        data.pop('longitude')
        data.pop('latitude')
        return Contactus.objects.create(**data)   


class ContactusViewSerialzier(GeoFeatureModelSerializer):
    class Meta:
        model = Contactus
        fields = '__all__'
        geo_field = 'location'