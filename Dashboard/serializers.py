from rest_framework import serializers
from SocialMonitoring.models import *

class PAPDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PAP
        fields = ('categoryOfPap' ,)

class RehabilationDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rehabilitation
        fields = '__all__'


class LabourcampDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabourCamp
        fields = ('id','labourCampName','toiletCondition' ,'drinkingWaterCondition' ,'demarkationOfPathwaysCondition',
                'signagesLabelingCondition','kitchenAreaCondition','fireExtinguishCondition','roomsOrDomsCondition',
                'segregationOfWasteCondition')