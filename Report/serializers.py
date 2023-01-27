from rest_framework.serializers import ModelSerializer
from SocialMonitoring.models import *
from EnvMonitoring.models import *
from rest_framework.validators import ValidationError
from Report.models import *

class LabourcampReportSerializer(ModelSerializer):
    class Meta:
        model = LabourCamp
        fields =('id','location','quarter', 'packages','dateOfMonitoring', 'labourCampName', 'labourCampId',
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

    def validate(self, data):
        if data['packages'] == '' or data['packages'] == None:
            raise ValidationError('packages can not be empty')
        if data['labourCampName'] == '' or data['labourCampName'] ==None:
            raise ValidationError('labourCampName can not be empty')
        return data


class ConstructionCampReportSerializer(ModelSerializer):
    class Meta:
        model = ConstructionSiteDetails
        fields = ('id','location','quarter', 'packages','dateOfMonitoring' ,'constructionSiteName' , 'constructionSiteId',
                    'isDemarkationOfPathways','demarkationOfPathwaysCondition','demarkationOfPathwaysPhotographs','demarkationOfPathwaysRemark' ,
                    'isSignagesLabeling','signagesLabelingCondition' ,'signagesLabelingPhotographs','signagesLabelingRemarks',
                    'isRegularHealthCheckup','regularHealthCheckupCondition','regularHealthCheckupPhotographs','regularHealthCheckupRemarks',
                    'isAvailabilityOfDoctor', 'availabilityOfDoctorCondition','availabilityOfDoctorPhotographs','availabilityOfDoctorRemarks',
                        'isFirstAidKit','firstAidKitCondition' ,'firstAidKitPhotographs','firstAidKitRemarks',
                    'isDrinkingWater','drinkingWaterCondition' ,'drinkingWaterPhotographs','drinkingWaterRemarks',
                        'isToilet', 'toiletCondition','toiletPhotograph','toiletRemarks',
                        'genralphotographs','documents','remarks')

                    

class PAPReportSerializer(ModelSerializer):
    class Meta:
        model = PAP
        fields = ('id','quarter', 'packages', 'location','dateOfMonitoring','dateOfIdentification','PAPID','nameOfPAP', 
                  'addressLine1','streetName','pincode','eligibility', 'categoryOfPap', 
                  'areaOfAsset','typeOfAsset','legalStatus','legalDocuments',
                   'actionTaken', 'notAgreedReason','remarks' )


class RehabilitationReportSerializer(ModelSerializer):
    class Meta:
        model = Rehabilitation
        fields =  ('id','location','ID','dateOfRehabilitation' ,'PAPID', 'PAPName' ,'cashCompensation', 'compensationStatus',
                   'typeOfCompensation', 'otherCompensationType' ,'addressLine1','streetName','pincode',
                   'isShiftingAllowance','shiftingAllowanceAmount','isLivelihoodSupport', 'livelihoodSupportAmount','livelihoodSupportCondition',
                   'livelihoodSupportPhotograph','livelihoodSupportRemarks','isTraining','trainingCondition',
                   'trainingPhotograph' ,'trainingRemarks' , 'typeOfTenaments'  ,'areaOfTenament' , 'tenamentsPhotograph',
                    'isRelocationAllowance' ,'RelocationAllowanceAmount' ,'isfinancialSupport',
                   'financialSupportAmount','isCommunityEngagement','isEngagementType', 'photographs' , 'documents','remarks')


        

'''----------------------- Env Monitoring Report Serilaizer------------------------------'''

class AirReportSerializer(ModelSerializer):
    class Meta:
        model = Air
        fields =('id','quarter','packages','month','location','dateOfMonitoring','PM10','standardPM10','SO2',
                   'standardSO2','O3','standardO3','NOx', 'standardNOx','AQI' , 'Remarks')


class NoiseReportSerializer(ModelSerializer):
    class Meta:
        model = Noise
        fields = ('id','location' ,'quarter','month','packages','dateOfMonitoringThree' ,'noiseLevel' , 'monitoringPeriod', )

class waterReportSerializer(ModelSerializer):
    class Meta:
        model = water
        fields =('id','location','quarter','packages','month', 'dateOfMonitoringTwo','qualityOfWater' , 'sourceOfWater' ,'waterDisposal')


class wasteTreatmentsSerializer(ModelSerializer):
    class Meta:
        model = WasteTreatments
        fields = ('id','location','quarter','month','packages','dateOfMonitoring' , 'wastetype' ,'quantity',
                    'wastehandling' , 'wasteHandlingLocation', 'photographs' , 'documents','remarks')


class materialManagementSerializer(ModelSerializer):
    class Meta:
        model = MaterialManegmanet
        fields = ('id','quarter','month','packages','location','dateOfMonitoring',
         'typeOfMaterial','source','sourceOfQuarry','materialStorageType','storageLocation',
         'materialstorageCondition','materialstoragePhotograph','approvals' ,'photographs',
          'documents','remarks')


class treeManagementSerializer(ModelSerializer):
    class Meta:
        model = ExistingTreeManagment
        fields = ('id','quarter','month','dateOfMonitoring','packages','location','treeID','commanName' ,'botanicalName',
                    'condition', 'noOfTreeCut','actionTaken', 'photographs', 'documents','remarks')

class Package54AlignmentSerializer(ModelSerializer):
    class Meta:
        model = Package54Alignment
        fields = ('gid' ,'name' , 'geom' )

class Package12AlignmentSerializer(ModelSerializer):
    class Meta:
        model = Package12Alignment
        fields = ('gid' ,'name' , 'geom')

class Package11AlignmentSerializer(ModelSerializer):
    class Meta:
        model = Package11Alignment
        fields = ('gid' ,'name' , 'geom')


class Package10AlignmentSerializer(ModelSerializer):
    class Meta:
        model = Package10Alignment
        fields = ('gid' ,'name' , 'geom')

class Package09AlignmentSerializer(ModelSerializer):
    class Meta:
        model = Package09Alignment
        fields = ('gid' ,'name' , 'geom')



class Package08AlignmentSerializer(ModelSerializer):
    class Meta:
        model = Package08Alignment
        fields = ('gid' ,'name' , 'geom')

class MetroStationSerializer(ModelSerializer):
    class Meta:
        model = Station
        fields = ('gid' , 'name', 'geom')


class ProjectAffectedTreesSerializer(ModelSerializer):
    class Meta:
        model = ProjectAffectedTrees
        fields = ('gid','tree_no_field' , 'common_nam' , 'botanical' ,'proposed_a','condition','survey_dat','layer','geom')