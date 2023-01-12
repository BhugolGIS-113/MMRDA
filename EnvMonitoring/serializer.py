from rest_framework import serializers 
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import (User , Air , Noise , water , TreeManagment , WasteTreatments , MaterialManegmanet ,)

class AirSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    class Meta:
        model = Air
        fields = ('user','quarter','packages','month','longitude','latitude','dateOfMonitoring','PM10','standardPM10','SO2',
                   'standardSO2','O3','standardO3','NOx', 'standardNOx','AQI' , 'Remarks')
        # geo_field='location'
    
    def create(self,data):
        data.pop('latitude')
        data.pop('longitude')
        return Air.objects.create(**data)

    
        
class AirViewSerializer(GeoFeatureModelSerializer):
    class Meta:
        model=Air
        fields='__all__'
        geo_field='location'

class WaterSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    class Meta:
        model = water
        fields = ('user' ,'quarter','packages','month', 'dateOfMonitoring','longitude','latitude',
        'qualityOfWater' , 'sourceOfWater' ,'waterDisposal')

    def create(self,data):
        data.pop('latitude')
        data.pop('longitude')
        return water.objects.create(**data)

    def validate(self,data):
        if data['quarter']=="" or data['quarter']==None:
            raise serializers.ValidationError("quarter cannot be empty!!")
        if data['packages'] == "" or data['packages'] == None:
            raise serializers.ValidationError('package cannot be empty!!')
        if data['longitude'] == "" or data['longitude'] == None:
            raise serializers.ValidationError('longitude cannot be empty!!')
        if data['latitude'] == "" or data['latitude'] == None:
            raise serializers.ValidationError('latitude cannot be empty!!')
        # if data['water_id'] == "" or data['water_id'] == None:
        #     raise serializers.ValidationError('water_id cannot be empty!!')
        if data['qualityOfWater'] == "" or data['qualityOfWater'] == None:
            raise serializers.ValidationError('quality_of_water cannot be empty!!')
        if data['sourceOfWater'] == "" or data['sourceOfWater'] == None:
            raise serializers.ValidationError('source_of_water cannot be empty!!')
        return data
        

class waterviewserializer(GeoFeatureModelSerializer):
    class Meta:
        model = water
        fields = '__all__'
        geo_field='location'


class NoiseSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    class Meta:
        model = Noise
        fields = ('user','quarter','month','packages','longitude','latitude' ,'dateOfMonitoring','noiseLevel' , 'monitoringPeriod', )

    def create(self,data):
        data.pop('latitude')
        data.pop('longitude')
        return Noise.objects.create(**data)

    def validate(self,data):
        if data['quarter']=="" or data['quarter']==None:
            raise serializers.ValidationError("quarter cannot be empty!!")
        if data['packages'] == "" or data['packages'] == None:
            raise serializers.ValidationError('package cannot be empty!!')
        if data['longitude'] == "" or data['longitude'] == None:
            raise serializers.ValidationError('longitude cannot be empty!!')
        if data['latitude'] == "" or data['latitude'] == None:
            raise serializers.ValidationError('latitude cannot be empty!!')
        # if data ['noise_id'] == "" or data['noise_id'] == None:
        #     raise serializers.ValidationError('noise_id cannot be empty!!')
        if data['noiseLevel'] == "" or data['noiseLevel'] == None:
            raise serializers.ValidationError('noise_level cannot be empty!!')
        if data['monitoringPeriod'] == "" or data['monitoringPeriod'] == None:
            raise serializers.ValidationError('Monitoring_Period cannot be empty!!')
        return data

class Noiseviewserializer(GeoFeatureModelSerializer):
    class Meta:
        model = Noise
        fields = '__all__'
        geo_field='location'

class TreeManagementSerailizer(serializers.ModelSerializer):
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    # Clongitude = serializers.CharField(max_length=10,required=False)
    # Clatitude = serializers.CharField(max_length=10,required=False)


    class Meta:
        model = TreeManagment
        fields = ('quarter','month','dateOfMonitoring','packages','longitude','latitude' ,'EtreeID','EcommanName' ,'EbotanicalName',
                    'Econdition', 'noOfTreeCut','actionTaken', 'Ephotographs', 'Edocuments','Eremarks')
                    # 'Clongitude','Clatitude','Cname','CbotonicalName','Ccondition','Cphotographs','Cdocuments','Cremarks')
        
    def create(self,data):
        data.pop('latitude')
        data.pop('longitude')
        # data.pop('Clongitude')
        # data.pop('Clatitude')
        return TreeManagment.objects.create(**data)

    


class TreeManagmentviewserializer(GeoFeatureModelSerializer):
    class Meta:
        model = TreeManagment
        fields = '__all__'
        geo_field = 'location'

class WasteTreatmentsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    waste_longitude = serializers.CharField(max_length=10,required=False)
    waste_latitude = serializers.CharField(max_length=10,required=False)
    class Meta:
        model  = WasteTreatments
        fields = ('user','quarter','month','packages','longitude','latitude'  ,'dateOfMonitoring' , 'wastetype' ,'quantity',
         'wastehandling' , 'waste_longitude' ,'waste_latitude', 'photographs' , 'documents','remarks')

    def create(self,data):
        data.pop('longitude')
        data.pop('latitude')
        data.pop('waste_longitude')
        data.pop('waste_latitude')
        return WasteTreatments.objects.create(**data)




class wastetreatmentsViewserializer(GeoFeatureModelSerializer):
    class Meta: 
        model = WasteTreatments
        fields = '__all__'
        geo_field= 'location'



class MaterialManagmentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    storageLongitude = serializers.CharField(max_length=10,required=False)
    storageLatitude = serializers.CharField(max_length=10,required=False)

    class Meta:
        model = MaterialManegmanet
        fields = ('user','quarter','month','packages','longitude','dateOfMonitoring','latitude' ,
         'typeOfMaterial','source','sourceOfQuarry','materialStorageType','storageLongitude' ,'storageLatitude',
         'materialstorageCondition','materialstoragePhotograph','approvals' ,'photographs',
          'documents','remarks')



    def create(self,data):
        data.pop('longitude')
        data.pop('latitude')
        data.pop('storageLongitude')
        data.pop('storageLatitude')
        return MaterialManegmanet.objects.create(**data)

    

class MaterialSourcingViewserializer(GeoFeatureModelSerializer):
    class Meta:
        model = MaterialManegmanet
        fields = '__all__'
        geo_field = 'location'


class TreemanagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreeManagment
        fields = ['quarter','packages','location']

class AirmanagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Air
        fields = ['quarter','packages']


class NoisemanagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noise
        fields = ['noiseLevel','monitoringPeriod','location','packages','quarter']


class WasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteTreatments
        fields = ['wastetype','quantity','wastehandling','location','packages','quarter','photographs','remarks']

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialManegmanet
        fields = ['approvals','sourceOfQuarry','typeOfMaterial','location','packages','quarter']

class WatermanamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = water
        fields = ['qualityOfWater','sourceOfWater','location','packages','quarter']