from rest_framework import serializers
from .models import PAP, ConstructionSiteDetails, LabourCamp ,Rehabilitation
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class social_MonitoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = PAP
        fields = '__all__'


class PapSerailzer(serializers.ModelSerializer):
    longitude = serializers.CharField(max_length=10, required=False)
    latitude = serializers.CharField(max_length=10, required=False)

    class Meta:
        model = PAP
        fields = ('quarter', 'packages', 'longitude', 'latitude','dateOfMonitoring','dateOfIdentification','PAPID','nameOfPAP', 
                  'addressLine1','streetName','pincode','eligibility', 'categoryOfPap',  'typeOfAsset','privateLand', 'GovernmentLand',
                  'individualLandAsset','privateLand','GovernmentLand','typeOfAsset','legalStatus','legalDocuments',
                   'actionTaken', 'notAgreedReason','presentPhotograp','remarks')

    def create(self, data):
        data.pop('longitude')
        data.pop('latitude')
        return PAP.objects.create(**data)
    
   

class PapUpdateSerialzier(serializers.ModelSerializer):
    longitude = serializers.CharField(max_length=10, required=False)
    latitude = serializers.CharField(max_length=10, required=False)
    class Meta:
        model = PAP
        fields = ('quarter', 'packages', 'longitude', 'latitude','dateOfMonitoring','PAPID', 'dateOfIdentification',
                  'addressLine1','streetName','pincode','eligibility', 'categoryOfPap',  'typeOfAsset','privateLand', 'GovernmentLand',
                  'individualLandAsset','privateLand','GovernmentLand','typeOfAsset','legalStatus','legalDocuments',
                   'actionTaken', 'notAgreedReason','presentPhotograp','remarks')
class papviewserialzer(GeoFeatureModelSerializer):
    class Meta:
        model = PAP
        fields = '__all__'
        geo_field = 'location'

class RehabilitationSerializer(serializers.ModelSerializer):
    longitude = serializers.CharField(max_length=10, required=False)
    latitude = serializers.CharField(max_length=10, required=False)
    class Meta:
        model = Rehabilitation
        fields = ('longitude', 'latitude','PAPID','dateOfRehabilitation' , 'PAPName' ,'cashCompensation', 'compensationStatus',
                   'typeOfCompensation', 'otherCompensationType' ,'addressLine1','streetName','pincode',
                   'isShiftingAllowance','shiftingAllowanceAmount','isLivelihoodSupport', 'livelihoodSupportCondition',
                   'livelihoodSupportPhotograph','livelihoodSupportRemarks','isTraining','trainingCondition',
                   'trainingPhotograph' ,'trainingRemarks' , 'isTenaments' , 'tenamentsCondition' , 'tenamentsPhotograph',
                   'tenamentsRemarks', 'isRelocationAllowance' ,'RelocationAllowanceAmount' ,'isfinancialSupport',
                   'financialSupportAmount','isCommunityEngagement','isEngagementType', 'photographs' , 'documents','remarks')

    def create(self, data):
        data.pop('longitude')
        data.pop('latitude')
        return Rehabilitation.objects.create(**data)
class RehabilitationViewSerializer(GeoFeatureModelSerializer):
    class Meta:
            model = Rehabilitation
            fields = '__all__'
            geo_field = 'location'

class constructionSiteSerializer(serializers.ModelSerializer):
    longitude = serializers.CharField(max_length=10, required=False)
    latitude = serializers.CharField(max_length=10, required=False)

    class Meta:
        model = ConstructionSiteDetails
        fields = ('quarter', 'packages','dateOfMonitoring' ,'longitude', 'latitude', 'constructionSiteName' , 'constructionSiteID',
                  'isDemarkingOfPathwaysCheck','isSignagesLabelingCheck', 'isRegularHealthCheckup',
                  'isAvailabilityOfDoctor', 'isFirstAidKit', 'isDrinkingWaterCheck', 'isToiletFacility',
                    'photographs','documents','remarks')
    
    def create(self,data):
        data.pop('longitude', None)
        data.pop('latitude', None)
        return ConstructionSiteDetails.objects.create(**data)
    
    def validate(self,data):
        if data['quarter']=="" or data['quarter']==None:
            raise serializers.ValidationError("quarter cannot be empty!!")
        if data['packages'] == "" or data['packages'] == None:
            raise serializers.ValidationError('package cannot be empty!!')
        if data['longitude'] == "" or data['longitude'] == None:
            raise serializers.ValidationError('longitude cannot be empty!!')
        if data['latitude'] == "" or data['latitude'] == None:
            raise serializers.ValidationError('latitude cannot be empty!!')
        # if data['LabourCampTitle'] == "" or data['LabourCampTitle'] == None:
        #     raise serializers.ValidationError('LabourCampTitle cannot be empty!!')
        # if data['sitephotographs'] == "" or data['sitephotographs'] == None:  
        #     raise serializers.ValidationError('site_photographs cannot be empty!!')
        if data['isSignagesLabelingCheck'] == "" or data['isSignagesLabelingCheck'] == None:
            raise serializers.ValidationError('signAges_or_labeling cannot be empty!!')
        if data['isDemarkingOfPathwaysCheck'] == "" or data['isDemarkingOfPathwaysCheck'] == None:
            raise serializers.ValidationError('demarking_of_pathways cannot be empty!!')
        if data['isRegularHealthCheckup'] == "" or data['isRegularHealthCheckup'] == None:
            raise serializers.ValidationError('Regular_Health_Checkup cannot be empty!!')
        if data['isAvailabilityOfDoctor'] == "" or data['isAvailabilityOfDoctor'] == None:
            raise serializers.ValidationError('Availability_Of_Doctor cannot be empty!!')   
        if data['isFirstAidKit'] == "" or data['isFirstAidKit'] == None:
            raise serializers.ValidationError('Availability_Of_First_aid_Kit cannot be empty!!')
        if data['isDrinkingWaterCheck'] == "" or data['isDrinkingWaterCheck'] == None:
            raise serializers.ValidationError('Drinking_water cannot be empty!!')
        if data['isToiletFacility'] == "" or data['isToiletFacility'] == None:
            raise serializers.ValidationError('Toilet_facility cannot be empty!!')
        return data

class ConstructionSiteDetailsViewSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ConstructionSiteDetails
        fields = '__all__'
        geo_field = 'location'


class LabourCampDetailSerializer(serializers.ModelSerializer):
    longitude = serializers.CharField(max_length=10, required=False)
    latitude = serializers.CharField(max_length=10, required=False)
    class Meta:
        model = LabourCamp
        fields = ('quarter', 'packages','dateOfMonitoring','longitude', 'latitude', 'labourCampName', 'LabourCampID',
                  'isToilet', 'toiletCondition','toiletPhotograph','toiletRemarks',
                  'isDrinkingWater','drinkingWaterCondition' ,'drinkingWaterPhotographs','drinkingWaterRemarks',
                    'isDemarkationOfPathways','demarkationOfPathwaysCondition','demarkationOfPathwaysPhotographs','demarkationOfPathwaysRemark' ,
                    'isSignagesLabeling','signagesLabelingCondition' ,'signagesLabelingPhotographs','signagesLabelingRemarks',
                    'isKitchenArea','kitchenAreaCondition','kitchenAreaPhotographs','kitchenAreaRemarks',
                    'isFireExtinguish','fireExtinguishCondition','fireExtinguishPhotographs','fireExtinguishRemarks',
                     'isRoomsOrDoms' ,'roomsOrDomsCondition','roomsOrDomsPhotographs' ,'roomsOrDomsRemarks',
                     'isSegregationOfWaste','segregationOfwasteCondition','segregationOfwastePhotographs','segregationOfwasteRemarks',
                    'isRegularHealthCheckup','regularHealthCheckupCondition','regularHealthCheckupPhotographs','regularHealthCheckupRemarks',
                     'isAvailabilityOfDoctor', 'availabilityOfDoctorCondition','availabilityOfDoctorPhotographs','availabilityOfDoctorRemarks',
                      'isFirstAidKit','firstAidKitCondition' ,'firstAidKitPhotographs','firstAidKitRemarks',
                    'transportationFacility' ,'transportationFacilityCondition', 'modeOfTransportation','distanceFromSite',
                    'GenralPhotographs' ,'documents','remarks')

    def create(self,data):
        data.pop('longitude')
        data.pop('latitude')
        return LabourCamp.objects.create(**data)
        
    # def validate(self , data):
    #     if data['quarter']=="" or data['quarter']==None:
    #         raise serializers.ValidationError("quarter cannot be empty!!")
    #     if data['packages'] == "" or data['packages'] == None:
    #         raise serializers.ValidationError('package cannot be empty!!')
    #     if data['longitude'] == "" or data['longitude'] == None:
    #         raise serializers.ValidationError('longitude cannot be empty!!')
    #     if data['latitude'] == "" or data['latitude'] == None:
    #         raise serializers.ValidationError('latitude cannot be empty!!')
    #     if data['isToilet'] == "" or data['isToilet'] == None:
    #         raise serializers.ValidationError('toilets cannot be empty!!')
    #     if data['labourCampName'] == "" or data['labourCampName'] == None:
    #         raise serializers.ValidationError('labourcamp Title cannot be empty!!')
    #     if data['isDrinkingWater'] == "" or data['isDrinkingWater'] == None:
    #         raise serializers.ValidationError('Drinking_water cannot be empty!!')
    #     if data ['isDemarkationOfPathways'] == "" or data['isDemarkationOfPathways'] == None:
    #         raise serializers.ValidationError('demarking_of_pathways cannot be empty!!')
    #     if data['isSignagesLabeling'] == "" or data['isSignagesLabeling'] == None:
    #         raise serializers.ValidationError('signAges_or_labeling cannot be empty!!')
    #     if data['isRegularHealthCheckup'] == "" or data['isRegularHealthCheckup'] == None:
    #         raise serializers.ValidationError('Regular_Health_Checkup cannot be empty!!')
    #     if data['isAvailabilityOfDoctor'] == "" or data['isAvailabilityOfDoctor'] == None:
    #         raise serializers.ValidationError('Availability_Of_First_aid_Kit cannot be empty!!')
    #     if data['isFirstAidKit'] == "" or data['isFirstAidKit'] == None:
    #         raise serializers.ValidationError('Availability_Of_Doctor cannot be empty!!')
    #     if data['isKitchenArea'] == "" or data['isKitchenArea'] == None:
    #         raise serializers.ValidationError('kitchen_area cannot be empty !!')
    #     if data['isFireExecution'] == "" or data['isFireExecution'] == None:
    #         raise serializers.ValidationError('fire_execution cannot be empty!!')
    #     if data['isSegregationOfWaste'] == "" or data['isSegregationOfWaste'] == None:
    #         raise serializers.ValidationError('segregation_of_waste cannot be empty!!')
    #     if data['isRoomsOrDoms'] == "" or data['isRoomsOrDoms'] == None:
    #         raise serializers.ValidationError('rooms_or_doms cannot be empty!!')
    #     if data[ 'transportationFacility'] == "" or data['transportationFacility'] == None:
    #         raise serializers.ValidationError('transport_facility cannot be empty')

        # return data

class LabourCampDetailViewSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LabourCamp
        fields = '__all__'
        geo_field = 'location'

# class testserialzier(serializers.ModelSerializer):
#     class Meta:
#         model = Test
#         fields = '__all__'

class PAPSerializer(serializers.ModelSerializer):
    class Meta:
        model = PAP
        fields = '__all__'




class ConstructionSiteDetailsserializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionSiteDetails
        fields = '__all__'




class LabourCampserializer(serializers.ModelSerializer):
    class Meta:
        model = LabourCamp
        fields = '__all__'