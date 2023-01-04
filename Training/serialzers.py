
from rest_framework import serializers
from .models import traning , photographs , occupationalHealthSafety
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
        'JoiningMedicalCheckup' , 'PPEkit' ,'TrainingToWorkers','HouseKeeping' ,'PowerSupplySystem' ,'AssemblyArea' ,
        'AmbulanceArrangement' ,'ToiletFacility','SafeMomentPasage' ,'MaterialKeepingPractice','accidental_check','SafetyGearStatus',
        'Barricading','NatureOfAccident' ,'TypeOfIncident' ,'IncidentDetails' ,'IdentifiedCauseOfIncident' ,'Outcome' ,'CompensationPaid' ,
        'photographs' ,'Remarks']

    
    def create(self,data):
        data.pop('longitude')
        data.pop('latitude')
        return occupationalHealthSafety.objects.create(**data)

class occupationalHealthSafetyViewSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = occupationalHealthSafety
        fields = '__all__'
        geo_field = 'location'
 