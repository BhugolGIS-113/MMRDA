
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
 
class ContactusImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contactus
        fields = "__all__"

class ContactusSerializezr(serializers.ModelSerializer):
    images =  ContactusImageSerializers(many=True, read_only=True)
    longitude = serializers.CharField(max_length= 255 , required = False) # longitude
    latitude = serializers.CharField(max_length= 255, required = False) # latitude
    uploaded_images  = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )
    class Meta:
        model = Contactus
        fields = ('name','email','messsage' , 'longitude' , 'latitude', 'images' , 'uploaded_images')

    def create(self,data):
        data.pop('longitude')
        data.pop('latitude')
        uploaded_images = data.pop("uploaded_images")
        print(uploaded_images )
        contactus = Contactus.objects.create(**data)
        print(contactus)

        for image in uploaded_images:
            ContactusImage.objects.create(contactus=contactus, images=image)
        return contactus
        


class ContactusViewSerialzier(GeoFeatureModelSerializer):
    class Meta:
        model = Contactus
        fields = '__all__'
        geo_field = 'location'