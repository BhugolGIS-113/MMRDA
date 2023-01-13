from rest_framework.serializers import ModelSerializer
from SocialMonitoring.models import *
from EnvMonitoring.models import *

class LabourcampReportSerializer(ModelSerializer):
    class Meta:
        model = LabourCamp
        fields =('location','quarter', 'packages','dateOfMonitoring', 'labourCampName', 'LabourCampID',
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


class ConstructionCampReportSerializer(ModelSerializer):
    class Meta:
        model = ConstructionSiteDetails
        fields = ('location','quarter', 'packages','dateOfMonitoring' ,'constructionSiteName' , 'constructionSiteID',
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
        fields = ('quarter', 'packages', 'location','dateOfMonitoring','dateOfIdentification','PAPID','nameOfPAP', 
                  'addressLine1','streetName','pincode','eligibility', 'categoryOfPap', 
                  'areaOfAsset','typeOfAsset','legalStatus','legalDocuments',
                   'actionTaken', 'notAgreedReason','presentPhotograp','remarks' )


class RehabilitationReportSerializer(ModelSerializer):
    class Meta:
        model = Rehabilitation
        fields =  ('location','ID','dateOfRehabilitation' ,'PAPID', 'PAPName' ,'cashCompensation', 'compensationStatus',
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
        fields =('quarter','packages','month','location','dateOfMonitoring','PM10','standardPM10','SO2',
                   'standardSO2','O3','standardO3','NOx', 'standardNOx','AQI' , 'Remarks')


class NoiseReportSerializer(ModelSerializer):
    class Meta:
        model = Noise
        fields = ('location' ,'quarter','month','packages','dateOfMonitoring' ,'noiseLevel' , 'monitoringPeriod', )

class waterReportSerializer(ModelSerializer):
    class Meta:
        model = water
        fields =('location','quarter','packages','month', 'dateOfMonitoring','qualityOfWater' , 'sourceOfWater' ,'waterDisposal')


class wasteTreatmentsSerializer(ModelSerializer):
    class Meta:
        model = WasteTreatments
        fields = ('location','quarter','month','packages','dateOfMonitoring' , 'wastetype' ,'quantity',
                    'wastehandling' , 'wasteHandlingLocation', 'photographs' , 'documents','remarks')


class materialManagementSerializer(ModelSerializer):
    class Meta:
        model = MaterialManegmanet
        fields = ('quarter','month','packages','location','dateOfMonitoring',
         'typeOfMaterial','source','sourceOfQuarry','materialStorageType','storageLocation',
         'materialstorageCondition','materialstoragePhotograph','approvals' ,'photographs',
          'documents','remarks')