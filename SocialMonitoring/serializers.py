from rest_framework import serializers
from .models import PAP, ConstructionSiteDetails, LabourCamp ,Rehabilitation , labourcampDetails
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.fields import CurrentUserDefault







#---------------Labour camp Serializer for GEO jason Format--------------------------------
class labourCampDetailSerializer(serializers.ModelSerializer):
    longitude = serializers.CharField(max_length=10, required=False)
    latitude = serializers.CharField(max_length=10, required=False)
    class Meta:
        model = labourcampDetails
        fields = ('LabourCampName' , 'LabourCampID' , 'longitude' , 'latitude')

    def create(self, data):
        data.pop('longitude')
        data.pop('latitude')
        return labourcampDetails.objects.create(**data) 

class labourCampDetailviewSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = labourcampDetails
        fields = '__all__'
        geo_field = 'location'


class labourCampDetailGetviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = labourcampDetails
        fields = '__all__'







# --------------- PAP Serializer --------------------------------

class PapSerailzer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    longitude = serializers.CharField(max_length=10, required=False)
    latitude = serializers.CharField(max_length=10, required=False)

    class Meta:
        model = PAP
        fields = ('quarter', 'packages', 'longitude', 'latitude','dateOfMonitoring', 'user','dateOfIdentification','PAPID','nameOfPAP', 
                  'addressLine1','streetName','pincode','eligibility', 'categoryOfPap', 
                  'individualLandAsset','areaOfLand','typeOfAsset','legalStatus','legalDocuments',
                   'actionTaken', 'notAgreedReason','presentPhotograp','remarks' )


    def create(self, data):
        data.pop('longitude')
        data.pop('latitude')
        return PAP.objects.create(**data)
    
   

class PapUpdateSerialzier(serializers.ModelSerializer):
    longitude = serializers.CharField(max_length=10, required=False)
    latitude = serializers.CharField(max_length=10, required=False)
    class Meta:
        model = PAP
        fields = ('quarter', 'packages', 'longitude', 'latitude', 'dateOfIdentification',
                  'addressLine1','streetName','pincode','eligibility', 'categoryOfPap',
                  'individualLandAsset','areaOfLand','typeOfAsset','legalStatus','legalDocuments',
                   'actionTaken', 'notAgreedReason','presentPhotograp','remarks')


class papviewserialzer(GeoFeatureModelSerializer):
    class Meta:
        model = PAP
        fields = '__all__'
        geo_field = 'location'






# ------------------------ Rehabiliation Serializer ----------------------------------------
class RehabilitationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    longitude = serializers.CharField(max_length=10, required=False)
    latitude = serializers.CharField(max_length=10, required=False)
    class Meta:
        model = Rehabilitation
        fields = ('user','longitude', 'latitude','PAPID','dateOfRehabilitation' , 'PAPName' ,'cashCompensation', 'compensationStatus',
                   'typeOfCompensation', 'otherCompensationType' ,'addressLine1','streetName','pincode',
                   'isShiftingAllowance','shiftingAllowanceAmount','isLivelihoodSupport', 'livelihoodSupportAmount','livelihoodSupportCondition',
                   'livelihoodSupportPhotograph','livelihoodSupportRemarks','isTraining','trainingCondition',
                   'trainingPhotograph' ,'trainingRemarks' , 'typeOfTenaments'  ,'areaOfTenament' , 'tenamentsPhotograph',
                    'isRelocationAllowance' ,'RelocationAllowanceAmount' ,'isfinancialSupport',
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




# -------------------------------- Labour camp details Serialzier --------------------------------         

class LabourCampDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    longitude = serializers.CharField(max_length=10, required=False)
    latitude = serializers.CharField(max_length=10, required=False)
    
    class Meta:
        model = LabourCamp
        fields = ('user','quarter', 'packages','dateOfMonitoring','longitude', 'latitude', 'labourCampName', 'LabourCampID',
                  'isToilet', 'toiletCondition','toiletPhotograph','toiletRemarks',
                  'isDrinkingWater','drinkingWaterCondition' ,'drinkingWaterPhotographs','drinkingWaterRemarks',
                    'isDemarkationOfPathways','demarkationOfPathwaysCondition','demarkationOfPathwaysPhotographs','demarkationOfPathwaysRemark' ,
                    'isSignagesLabeling','signagesLabelingCondition' ,'signagesLabelingPhotographs','signagesLabelingRemarks',
                    'isKitchenArea','kitchenAreaCondition','kitchenAreaPhotographs','kitchenAreaRemarks',
                    'isFireExtinguish','fireExtinguishCondition','fireExtinguishPhotographs','fireExtinguishRemarks',
                     'isRoomsOrDoms' ,'roomsOrDomsCondition','roomsOrDomsPhotographs' ,'roomsOrDomsRemarks',
                     'isSegregationOfWaste','segregationOfWasteCondition','segregationOfWastePhotographs','segregationOfWasteRemarks',
                    'isRegularHealthCheckup','regularHealthCheckupCondition','regularHealthCheckupPhotographs','regularHealthCheckupRemarks',
                     'isAvailabilityOfDoctor', 'availabilityOfDoctorCondition','availabilityOfDoctorPhotographs','availabilityOfDoctorRemarks',
                      'isFirstAidKit','firstAidKitCondition' ,'firstAidKitPhotographs','firstAidKitRemarks',
                    'transportationFacility' ,'transportationFacilityCondition', 'modeOfTransportation','distanceFromSite',
                    'photographs' ,'documents','remarks')

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
    #     if data['LabourCampID'] == "" or data['LabourCampID'] == None:
    #         raise serializers.ValidationError('LabourCamp ID cannot be empty!!')
    #     return data

class LabourCampUpdateSerialzier(serializers.ModelSerializer):
    class Meta:
        model = LabourCamp
        fields = ('LabourCampID' , 'labourCampName','isToilet','toiletCondition','toiletPhotograph','toiletRemarks',
                 'isDrinkingWater','drinkingWaterCondition' , 'drinkingWaterPhotographs', 'drinkingWaterRemarks',
                 'isDemarkationOfPathways','demarkationOfPathwaysCondition','demarkationOfPathwaysPhotographs' ,'demarkationOfPathwaysRemark',
                 'isSignagesLabeling','signagesLabelingPhotographs' ,'signagesLabelingRemarks' ,
                 'isKitchenArea','kitchenAreaCondition','kitchenAreaPhotographs','kitchenAreaRemarks',
                'isFireExtinguish','fireExtinguishCondition','fireExtinguishPhotographs','fireExtinguishRemarks',
                     'isRoomsOrDoms' ,'roomsOrDomsCondition','roomsOrDomsPhotographs' ,'roomsOrDomsRemarks',
                     'isSegregationOfWaste','segregationOfWasteCondition','segregationOfWastePhotographs','segregationOfWasteRemarks',
                    'isRegularHealthCheckup','regularHealthCheckupCondition','regularHealthCheckupPhotographs','regularHealthCheckupRemarks',
                     'isAvailabilityOfDoctor', 'availabilityOfDoctorCondition','availabilityOfDoctorPhotographs','availabilityOfDoctorRemarks',
                      'isFirstAidKit','firstAidKitCondition' ,'firstAidKitPhotographs','firstAidKitRemarks',
                    'transportationFacility' ,'transportationFacilityCondition', 'modeOfTransportation','distanceFromSite',
                    'photographs' ,'documents','remarks')





# ----------------------------- Construction site serializer -----------------------------------
class constructionSiteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    longitude = serializers.CharField(max_length=10, required=False)
    latitude = serializers.CharField(max_length=10, required=False)

    class Meta:
        model = ConstructionSiteDetails
        fields = ('user','quarter', 'packages','dateOfMonitoring' ,'longitude', 'latitude', 'constructionSiteName' , 'constructionSiteID',
                 'isDemarkationOfPathways','demarkationOfPathwaysCondition','demarkationOfPathwaysPhotographs','demarkationOfPathwaysRemark' ,
                'isSignagesLabeling','signagesLabelingCondition' ,'signagesLabelingPhotographs','signagesLabelingRemarks',
                'isRegularHealthCheckup','regularHealthCheckupCondition','regularHealthCheckupPhotographs','regularHealthCheckupRemarks',
                  'isAvailabilityOfDoctor', 'availabilityOfDoctorCondition','availabilityOfDoctorPhotographs','availabilityOfDoctorRemarks',
                      'isFirstAidKit','firstAidKitCondition' ,'firstAidKitPhotographs','firstAidKitRemarks',
                   'isDrinkingWater','drinkingWaterCondition' ,'drinkingWaterPhotographs','drinkingWaterRemarks',
                    'isToilet', 'toiletCondition','toiletPhotograph','toiletRemarks',
                    'genralphotographs','documents','remarks')
    
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
        if data['constructionSiteName'] == "" or data['constructionSiteName'] == None:
            raise serializers.ValidationError('construction Site Name cannot be empty!!')
        if data['constructionSiteID'] == "" or data['constructionSiteID'] == None:  
            raise serializers.ValidationError('construction Site ID cannot be empty!!')
   
        return data








''' This serializer for view the data - Amol Bhore'''

class ConstructionSiteDetailsViewSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ConstructionSiteDetails
        fields = '__all__'
        geo_field = 'location'
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