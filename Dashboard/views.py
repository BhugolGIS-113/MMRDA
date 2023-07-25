from django.db.models import Count
from rest_framework.generics import GenericAPIView, ListAPIView
from .serializers import *
from EnvMonitoring.models import *
from Training.models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.parsers import MultiPartParser


# Create your views here.

class PAPCategoryDashboardView(ListAPIView):
    serializer_class = PAPDashboardSerializer
    queryset = PAP.objects.all()

    def get(self, request, *args, **kwargs):
        categoryOfPap = PAP.objects.values('categoryOfPap').annotate(
            count=Count('categoryOfPap'))
        Rehabilitations = Rehabilitation.objects.values('categoryOfPap').annotate(count=Count('categoryOfPap'))
       
        # dataset_Rehabilitations = [count['count'] for count in Rehabilitations]
        lable = [count['categoryOfPap'] for count in categoryOfPap]
        # dataset_PAP = [count['count'] for count in categoryOfPap]
        # lable_PAP = [count['categoryOfPap'] for count in categoryOfPap]

        dataset_PAP = [22 , 22 , 20 , 25 , 23 , 22]
        dataset_Rehabilitations = [13 ,13 , 8 , 17, 13 , 17]
        result = []
        for i in range(len(dataset_PAP)):
            percentage = int((dataset_Rehabilitations[i] / dataset_PAP[i]) * 100)
            result.append(percentage)
        totel_identified = sum(dataset_PAP)
        total_Rehabilitations = sum(dataset_Rehabilitations)
        total_percentage = int(total_Rehabilitations / totel_identified * 100)
        return Response({'status': 'success',
                        'Message': 'Data Fetched successfully',
                        'label' : lable ,
                        'dataset_PAP': dataset_PAP,
                        'dataset_Rehabilitations' : dataset_Rehabilitations ,
                        'percentage' : result ,
                        'totel_identified' : totel_identified, 
                        'total_Rehabilitations' : total_Rehabilitations , 
                        'total_percentage' : total_percentage , 
                         })



class CategoryWiseCompensationChart(APIView):
    
    def get(self, request, *args , **kwargs):
        Rehabilitations = Rehabilitation.objects.values('categoryOfPap').annotate(count=Count('categoryOfPap'))
        dataset_Rehabilitations = [count['count'] for count in Rehabilitations]
        label = [count['categoryOfPap'] for count in Rehabilitations]
        Compensation_Status = Rehabilitation.objects.values('compensationStatus').annotate(count=Count('compensationStatus'))

        label_Compensation_Status = [count['compensationStatus'] for count in Compensation_Status]
        print(label_Compensation_Status)
        dataset_Compensation_Status = [count['count'] for count in Compensation_Status]
        print(dataset_Compensation_Status)

        return Response({'status': 'success',
                        'Message': 'Data Fetched successfully',
                        'label' : label ,
                        'dataset_Rehabilitations': dataset_Rehabilitations,
                        'label_Compensation_Status' : label_Compensation_Status ,
                        'dataset_Compensation_Status': dataset_Compensation_Status
                        })

        


class IdentifiedPAPDashboardView(APIView):
    serializer_class = PAPDashboardSerializer

    def get(self, request, *args, **kwargs):
        IdentifiedPAP = PAP.objects.all().count()
        if IdentifiedPAP == 0:
            return Response({'Message': 'No data Found',
                            'status': 'success'})

        return Response({'status': 'success',
                        'Message': 'Data Fetched successfully',
                         'dataset': IdentifiedPAP}, status=200)


class RehabilitatedPAPDashboardView(GenericAPIView):
    serializer_class = RehabilationDashboardSerializer

    def get(self, request):
        counts = Rehabilitation.objects.values(
            'compensationStatus').annotate(count=Count('compensationStatus'))

        dataset = [count['count'] for count in counts]
        return Response({'status': 'success',
                        'Message': 'Data fetched successfully',
                         'dataset': dataset,
                         'Counts': counts})


class LabourCampFacilitiesDashboardView(GenericAPIView):
    serializer_class = LabourcampDashboardSerializer

    def get(self, request, labourCampName, *args, **kwargs):

        labour = LabourCamp.objects.filter(
            labourCampName=labourCampName).latest('id')
        data = LabourcampDashboardSerializer(labour).data
        values = list(data.values())
        dataset = []
        dataset.append(values.count('Good')), dataset.append(
            values.count('Average'))
        dataset.append(values.count('Bad'))

        return Response({'status': 'success',
                        'Message': 'data Fetched successfully',
                        'dataset': dataset,
                        'data': data}, status=200)
        
class ConstructionChartView(GenericAPIView):
    serializer_class = ConstructionSiteDashboardSerializer

    def get(self, request,constructionSiteName, *args, **kwargs):
        ConstructionCamp = ConstructionSiteDetails.objects.filter(constructionSiteName = constructionSiteName).latest('id')
        data = ConstructionSiteDashboardSerializer(ConstructionCamp).data
        values = list(data.values())
        dataset = []
        dataset.append(values.count('Good')) , dataset.append(values.count('Average')) , dataset.append(values.count('Bad'))
        return Response({'status': 'success',
                        'Message': 'data Fetched successfully',
                        'dataset': dataset,
                        'data': data}, status=200)
class CashCompensationTypeCharView(GenericAPIView):
    serializer_class = RehabilationDashboardSerializer

    def get(self, request):
        counts = Rehabilitation.objects.values(
            'typeOfCompensation').annotate(count=Count('typeOfCompensation'))
        dataset = [count['count'] for count in counts]

        return Response({'status': 'success',
                         'Message': 'data fetched Successfully',
                         'dataset': dataset})


class ExistingTreeCount(GenericAPIView):
    serializer_class = ExistingTreeSerializer

    def get(self, request):
        try:
            ExistingTreeCount = []
            NewtreeCount = []
            treecount = ExistingTreeManagment.objects.all().count()
            NewTreeCount = NewTreeManagement.objects.all().count()
            ExistingTreeCount.append(
                treecount), NewtreeCount.append(NewTreeCount)
            return Response({'status': 'success',
                            'Message': 'Data was successfully fetched',
                             'ExistingTreeCount': ExistingTreeCount,
                             'NewtreeCount': NewtreeCount,
                             }, status=200)
        except:
            return Response({'status': 'error',
                            'Message': 'Something went wrong'}, status=400)


class WasteTypeCount(APIView):

    def get(self, request):
        counts = WasteTreatments.objects.values('wastetype').annotate(count = Count('wastetype'))
        dataset = [count['count'] for count in counts]

        return Response({'status': 'success',
                            'Message': 'Data was successfully fetched',
                            'dataset': dataset,
                            'counts' : counts})
        


class WasteHandelingChart(APIView):
    def get(self, request):
        counts = WasteTreatments.objects.values('wastehandling').annotate(count = Count('wastehandling'))
        dataset = [count['count'] for count in counts]
        return Response({'status': 'success',
                            'Message': 'Data was successfully fetched',
                            'dataset': dataset,
                            'counts' : counts})
    

class MaterialSourceTypeCountChart(APIView):

    def get(self, request):
        counts = MaterialManegmanet.objects.values('source').annotate(count = Count('source'))
        dataset = [count['count'] for count in counts]
        return Response({'status': 'success',
                         'Message': 'Data was successfully fetched',
                         'dataset': dataset,
                         'counts' : counts}, status=200)
       


class MaterialConditionChart(APIView):
    def get(self, request):

        counts = MaterialManegmanet.objects.values('materialstorageCondition').annotate(count = Count('materialstorageCondition'))
        dataset = [count['count'] for count in counts]
        return Response({'status': 'success',
                            'Message': 'Data was successfully fetched',
                            'dataset': dataset,
                            'counts' : counts}, status=200)
    


class IncidenttypeCountchart(APIView):

    def get(self, request):
        counts = occupationalHealthSafety.objects.values('typeOfIncident').annotate(count = Count('typeOfIncident'))
        dataset = [count['count'] for count in counts]
        

        return Response({'status': 'success',
                        'Message': 'Data was successfully fetched',
                        'dataset': dataset,
                        'counts' : counts })
        


class WaterConditionChart(APIView):

    def get(self, request):
        counts = water.objects.values('qualityOfWater').annotate(count = Count('qualityOfWater'))
        dataset = [count['count'] for count in counts]
        return Response({'status': 'success',
                            'Message': 'Data was successfully fetched',
                            'dataset': dataset,
                            'counts': counts }, status=200)
        

class AirChartView(generics.GenericAPIView):
    serializer_class = AirChartSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, month, year, **kwargs):
        try:
            airdata = Air.objects.get(month=month, dateOfMonitoring__year=year)
        except:
            return Response({'Message': 'No data Avaialable for this Month or Year',
                            'status': 'error'},)
        dataset = []
        serializers = AirChartSerializer(airdata).data
        dataset.append(serializers.get('PM10')), dataset.append(
        serializers.get('SO2')), dataset.append(serializers.get('O3')),
        dataset.append(serializers.get('NOx')), dataset.append(
            serializers.get('AQI'))
        return Response({'status': 'success',
                         'Message': 'Data was successfully fetched',
                         'dataset': dataset,})
                        #  'PM10': serializers.get('PM10'), 'SO2': serializers.get('SO2'),
                        #  'O3':  serializers.get('O3'), 'Nox': serializers.get('NOx'),
                        #  'AQI': serializers.get('AQI')})



    
