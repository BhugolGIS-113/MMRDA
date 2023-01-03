from rest_framework import serializers 
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import (User , Air , Noise , water , TreeManagment , WasteTreatments , MaterialSourcing ,)

class AirSerializer(serializers.ModelSerializer):
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    class Meta:
        model = Air
        fields = ('quarter','packages','month','longitude','latitude','dateOfConduct','PM10','standardPM10','SO2',
                   'standardSO2','O3','standardO3','NOx', 'standardNOx','AQI' , 'Remarks')
        # geo_field='location'
    def create(self,data):
        data.pop('latitude')
        data.pop('longitude')
        return Air.objects.create(**data)

    def validate(self, data):
        if data['quarter']=="" or data['quarter']==None:
            raise serializers.ValidationError("quarter cannot be empty!!")
        if data['packages'] == "" or data['packages'] == None:
            raise serializers.ValidationError('package cannot be empty!!')
        if data['longitude'] == "" or data['longitude'] == None:
            raise serializers.ValidationError('longitude cannot be empty!!')
        if data['latitude'] == "" or data['latitude'] == None:
            raise serializers.ValidationError('latitude cannot be empty!!')
        if data['PM10'] == "" or data['PM10'] == None:
            raise serializers.ValidationError('PM10 Cannot be empty!!')
        if data['standardPM10'] == "" or data['standardPM10'] == None:
            raise serializers.ValidationError('standardPM10 cannot be empty!!')
        if data['SO2'] == "" or data['SO2'] == None:
            raise serializers.ValidationError('SO2 cannot be empty!!') 
        if data ['standardSO2']  == "" or data['standardSO2'] == None:
            raise serializers.ValidationError('standardSO2 cannot be empty!!')
        if data['O3']   == "" or data['O3'] == None:
            raise serializers.ValidationError('O3 cannot be empty!!')
        if  data['standardO3'] == "" or data['standardO3'] == None:
            raise serializers.ValidationError('standardO3 cannot be empty!!')
        if data ['NOx'] == "" or data['NOx'] == None:
            raise serializers.ValidationError('NOx cannot be empty !!')
        if data ['standardNOx']          == "" or data['standardNO   x'] == None: 
            raise serializers.ValidationError('standardNO x cannot be empty !!')    
        if   data['AQI'] == "" or data['AQI'] == None:
            raise serializers.ValidationError('AQI cannot be empty !!')      
        if data['Remarks']  == "" or data['Remarks'] == None:
            raise serializers.ValidationError('Remarks cannot be empty !!')   
        
               
        return data
class AirViewSerializer(GeoFeatureModelSerializer):
    class Meta:
        model=Air
        fields='__all__'
        geo_field='location'

class WaterSerializer(serializers.ModelSerializer):
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    class Meta:
        model = water
        fields = ('quarter','packages','month', 'dateOfConduct','longitude','latitude',
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
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    class Meta:
        model = Noise
        fields = ('quarter','month','packages','longitude','dateOfConduct','latitude' ,'noiseLevel' , 'monitoringPeriod', )

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
    Clongitude = serializers.CharField(max_length=10,required=False)
    Clatitude = serializers.CharField(max_length=10,required=False)


    class Meta:
        model = TreeManagment
        fields = ('quarter','month','dateOfConduct','packages','longitude','latitude' ,'EtreeID','EcommanName' ,'EbotanicalName',
                    'Econdition', 'noOfTreeCut','actionTaken', 'Ephotographs', 'Edocuments','Eremarks',
                    'Clongitude','Clatitude','Cname','CbotonicalName','Ccondition','Cphotographs','Cdocuments','Cremarks')
        
    def create(self,data):
        data.pop('latitude')
        data.pop('longitude')
        data.pop('Clongitude')
        data.pop('Clatitude')
        return TreeManagment.objects.create(**data)
    
    def validate(self,data):
        if data['quarter']=="" or data['quarter']==None:
            raise serializers.ValidationError("quarter cannot be empty!!")
        if data['packages'] == "" or data['packages'] == None:
            raise serializers.ValidationError('package cannot be empty!!')
        if data['longitude'] == "" or data['longitude'] == None:
            raise serializers.ValidationError('longitude cannot be empty!!')
        if data['latitude'] == "" or data['latitude'] == None:
            raise serializers.ValidationError('latitude cannot be empty!!')
        # if data['EtreeID'] == "" or data['EtreeID'] == None:
        #     raise serializers.ValidationError('TreeID cannot be empty')
        if data['EcommanName'] == "" or data['EcommanName'] == None:
            raise serializers.ValidationError('common_name cannot be empty!!')
        if data['EbotanicalName'] == "" or data['EbotanicalName'] == None:
            raise serializers.ValidationError('botanical_name cannot be empty!!')
        if data['Econdition'] == "" or data['Econdition'] == None:
            raise serializers.ValidationError('condition cannot be empty!!')
        if data['actionTaken'] == "" or data['actionTaken'] == None:  
            raise serializers.ValidationError('actionTaken cannot be empty') 
        if data['noOfTreeCut'] == "" or data['noOfTreeCut'] ==None:
            raise serializers.ValidationError('noOfTreeCut cannot be empty !!')
    
        if data['Cname'] == "" or data['Cname'] == None:
            raise serializers.ValidationError('Cname cannot be empty !!')
        if data['CbotonicalName']== "" or data['CbotonicalName'] == None:
            raise serializers.ValidationError('CbotonicalName cannot be emoty !!')
        if data['Ccondition'] == "" or data['Ccondition'] == None:
            raise serializers.ValidationError('Ccondition cannot be empty !!') 
        if data['Cremarks'] == "" or data['Cremarks'] == None:
            raise serializers.ValidationError('remarks cannot be empty !!')
        return data
        


class TreeManagmentviewserializer(GeoFeatureModelSerializer):
    class Meta:
        model = TreeManagment
        fields = '__all__'
        geo_field = 'location'

class WasteTreatmentsSerializer(serializers.ModelSerializer):
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    waste_longitude = serializers.CharField(max_length=10,required=False)
    waste_latitude = serializers.CharField(max_length=10,required=False)
    class Meta:
        model  = WasteTreatments
        fields = ('quarter','month','packages','longitude','latitude'  ,'dateOfConduct' , 'wastetype' ,'quantity',
         'wastehandling' , 'waste_longitude' ,'waste_latitude', 'photographs' , 'documents','remarks')

    def create(self,data):
        data.pop('longitude')
        data.pop('latitude')
        data.pop('waste_longitude')
        data.pop('waste_latitude')
        return WasteTreatments.objects.create(**data)

    def validate(self,data):
        if data['quarter']=="" or data['quarter']==None:
            raise serializers.ValidationError("quarter cannot be empty!!")
        if data['packages'] == "" or data['packages'] == None:
            raise serializers.ValidationError('package cannot be empty!!')
        if data['longitude'] == "" or data['longitude'] == None:
            raise serializers.ValidationError('longitude cannot be empty!!')
        if data['latitude'] == "" or data['latitude'] == None:
            raise serializers.ValidationError('latitude cannot be empty!!')
        # if data['waste_id'] == "" or data['waste_id'] == None:
        #     raise serializers.ValidationError('waste_id cannot be empty!!')
        if data['wastetype'] == "" or data['wastetype'] == None:
            raise serializers.ValidationError('waste_type cannot be empty!!')
        if data ['quantity'] == "" or data['quantity'] == None:
            raise serializers.ValidationError('quantity cannot be empty!!')
        if data['wastehandling'] == "" or data['wastehandling'] == None:
            raise serializers.ValidationError('waste_handled cannot be empty!!')
    
        
        return data

class wastetreatmentsViewserializer(GeoFeatureModelSerializer):
    class Meta: 
        model = WasteTreatments
        fields = '__all__'
        geo_field= 'location'



class MaterialSourcingSerializer(serializers.ModelSerializer):
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    class Meta:
        model = MaterialSourcing
        fields = ('quarter','month','packages','longitude','dateOfConduct','latitude' , 'typeOfMaterial','source',
        'sourceOfQuarry','approvals' , 'photographs', 'documents','remarks')

    def validate(self,data):
        if data['quarter']=="" or data['quarter']==None:
            raise serializers.ValidationError("quarter cannot be empty!!")
        if data['packages'] == "" or data['packages'] == None:
            raise serializers.ValidationError('package cannot be empty!!')
        if data['longitude'] == "" or data['longitude'] == None:
            raise serializers.ValidationError('longitude cannot be empty!!')
        if data['latitude'] == "" or data['latitude'] == None:
            raise serializers.ValidationError('latitude cannot be empty!!')
        # if data['materialsourcing_id'] == "" or data['materialsourcing_id'] == None:
        #     raise serializers.ValidationError('materialsourcing_id cannot be empty!!')
        if data['sourceOfQuarry'] == "" or data['sourceOfQuarry'] == None:
            raise serializers.ValidationError('source_of_quary cannot be empty!!')
        
        return data
    def create(self,data):
        data.pop('longitude')
        data.pop('latitude')
        return MaterialSourcing.objects.create(**data)

    

class MaterialSourcingViewserializer(GeoFeatureModelSerializer):
    class Meta:
        model = MaterialSourcing
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
        model = MaterialSourcing
        fields = ['approvals','sourceOfQuarry','typeOfMaterial','location','packages','quarter']

class WatermanamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = water
        fields = ['qualityOfWater','sourceOfWater','location','packages','quarter']