from rest_framework.serializers import ModelSerializer
from SocialMonitoring.models import *
from EnvMonitoring.models import *
from rest_framework.validators import ValidationError
from Report.models import *
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class LabourcampReportSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LabourCamp
        fields =('id','quarter', 'packages','dateOfMonitoring', 'labourCampName', 'labourCampId',
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
        geo_field= ('location')

    def validate(self, data):
        if data['packages'] == '' or data['packages'] == None:
            raise ValidationError('packages can not be empty')
        if data['labourCampName'] == '' or data['labourCampName'] ==None:
            raise ValidationError('labourCampName can not be empty')
        return data


class ConstructionCampReportSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ConstructionSiteDetails
        fields = ('id','quarter', 'packages','dateOfMonitoring' ,'constructionSiteName' , 'constructionSiteId',
                    'isDemarkationOfPathways','demarkationOfPathwaysCondition','demarkationOfPathwaysPhotographs','demarkationOfPathwaysRemark' ,
                    'isSignagesLabeling','signagesLabelingCondition' ,'signagesLabelingPhotographs','signagesLabelingRemarks',
                    'isRegularHealthCheckup','regularHealthCheckupCondition','regularHealthCheckupPhotographs','regularHealthCheckupRemarks',
                    'isAvailabilityOfDoctor', 'availabilityOfDoctorCondition','availabilityOfDoctorPhotographs','availabilityOfDoctorRemarks',
                        'isFirstAidKit','firstAidKitCondition' ,'firstAidKitPhotographs','firstAidKitRemarks',
                    'isDrinkingWater','drinkingWaterCondition' ,'drinkingWaterPhotographs','drinkingWaterRemarks',
                        'isToilet', 'toiletCondition','toiletPhotograph','toiletRemarks',
                        'genralphotographs','documents','remarks')
        geo_field= ('location')

                    

class PAPReportSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PAP
        fields = ('id','quarter', 'packages','dateOfMonitoring','dateOfIdentification','PAPID','nameOfPAP', 
                  'addressLine1','streetName','pincode','eligibility', 'categoryOfPap', 
                  'areaOfAsset','typeOfAsset','legalStatus','legalDocuments',
                   'actionTaken', 'notAgreedReason','remarks' )
        geo_field= ('location')

class RehabilitationReportSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Rehabilitation
        fields =  ('id','ID','dateOfRehabilitation' ,'PAPID', 'PAPName' ,'cashCompensation', 'compensationStatus',
                   'typeOfCompensation', 'otherCompensationType' ,'addressLine1','streetName','pincode',
                   'isShiftingAllowance','shiftingAllowanceAmount','isLivelihoodSupport', 'livelihoodSupportAmount','livelihoodSupportCondition',
                   'livelihoodSupportPhotograph','livelihoodSupportRemarks','isTraining','trainingCondition',
                   'trainingPhotograph' ,'trainingRemarks' , 'typeOfTenaments'  ,'areaOfTenament' , 'tenamentsPhotograph',
                    'isRelocationAllowance' ,'RelocationAllowanceAmount' ,'isfinancialSupport',
                   'financialSupportAmount','isCommunityEngagement','isEngagementType', 'photographs' , 'documents','remarks')
        geo_field= ('location')

        

'''----------------------- Env Monitoring Report Serilaizer------------------------------'''

class AirReportSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Air
        fields =('id','quarter','packages','month','dateOfMonitoring','PM10','standardPM10','SO2',
                   'standardSO2','O3','standardO3','NOx', 'standardNOx','AQI' , 'Remarks')
        geo_field= ('location')

class NoiseReportSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Noise
        fields = ('id','location' ,'quarter','month','packages','dateOfMonitoringThree' ,'noiseLevel' , 'monitoringPeriod', )
        geo_field= ('location')

class waterReportSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = water
        fields =('id','quarter','packages','month', 'dateOfMonitoringTwo','qualityOfWater' , 'sourceOfWater' ,'waterDisposal')
        geo_field= ('location')


class wasteTreatmentsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = WasteTreatments
        fields = ('id','quarter','month','packages','dateOfMonitoring' , 'wastetype' ,'quantity',
                    'wastehandling' , 'wasteHandlingLocation', 'photographs' , 'documents','remarks')
        geo_field= ('location')


class materialManagementSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MaterialManegmanet
        fields = ('id','quarter','month','packages','dateOfMonitoring',
         'typeOfMaterial','source','sourceOfQuarry','materialStorageType','storageLocation',
         'materialstorageCondition','materialstoragePhotograph','approvals' ,'photographs',
          'documents','remarks')
        geo_field= ('location')


class treeManagementSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ExistingTreeManagment
        fields = ('id','quarter','month','dateOfMonitoring','packages','treeID','commanName' ,'botanicalName',
                    'condition', 'noOfTreeCut','actionTaken', 'photographs', 'documents','remarks')
        geo_field= ('location')

class Package54AlignmentSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Package54Alignment
        fields = ('gid' ,'name' )
        geo_field= ('geom')

class Package12AlignmentSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Package12Alignment
        fields = ('gid' ,'name')
        geo_field= ('geom')

class Package11AlignmentSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Package11Alignment
        fields = ('gid' ,'name' )
        geo_field= ('geom')


class Package10AlignmentSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Package10Alignment
        fields = ('gid' ,'name' )
        geo_field= ('geom')


class Package09AlignmentSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Package09Alignment
        fields = ('gid' ,'name')
        geo_field= ('geom')



class Package08AlignmentSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Package08Alignment
        fields = ('gid' ,'name')
        geo_field= ('geom')


class MetroStationSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Station
        fields = ('gid' , 'name')
        geo_field= ('geom')


class ProjectAffectedTreesSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ProjectAffectedTrees
        fields = ('gid','tree_no_field' , 'common_nam' , 'botanical' ,'proposed_a','condition','survey_dat','layer')
        geo_field= ('geom')