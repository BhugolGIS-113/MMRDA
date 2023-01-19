from rest_framework.generics import GenericAPIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView



# Create your views here.

class PAPCategoryDashboardView(GenericAPIView):
    serializer_class = PAPDashboardSerializer
    queryset = PAP.objects.all()

    def get(self, request , *args, **kwargs):
            try:
                dataSet = []
                Residential = PAP.objects.filter(categoryOfPap = 'Residential').count()
                Commercial = PAP.objects.filter(categoryOfPap = 'Commercial').count()
                Private_Land = PAP.objects.filter(categoryOfPap = 'Private Land').count()
                Government_Land = PAP.objects.filter(categoryOfPap = 'Government Land').count()
                Institutional = PAP.objects.filter(categoryOfPap = 'Institutional').count()
                Other = PAP.objects.filter(categoryOfPap = 'Other').count()
                dataSet.append(Residential) , dataSet.append(Commercial) ,dataSet.append(Private_Land)
                dataSet.append(Government_Land) , dataSet.append(Other) , dataSet.append(Institutional)
               
                return Response({'status': 'success',
                                'Message' : 'Data Fetched successfully',
                                'dataset': dataSet,
                                # 'Residential' : Residential,
                                # 'Commercial' : Commercial,
                                # 'Private_Land':Private_Land,
                                # 'Government_Land' : Government_Land,
                                # 'Institutional' : Institutional,
                                # 'Other' : Other
                                }, status=200)
            except:
                return Response({'Message': 'Invalid category'}, status=400)


class IdentifiedPAPDashboardView(APIView):
    serializer_class = PAPDashboardSerializer

    def get(self, request, *args, **kwargs):
        try:
            IdentifiedPAP = PAP.objects.all().count()
            if IdentifiedPAP == 0:
                return Response({'Message': 'No data Found',
                                'status' : 'success'}, status=200)

            return Response({'status' : 'success' ,
                            'Message': IdentifiedPAP}, status=200)
        except:
            return Response({'Message': 'Something went Wrong'}, status=400)

class RehabilitatedPAPDashboardView(GenericAPIView):
    serializer_class = RehabilationDashboardSerializer
    def get(self , request ):
        try:
            dataset = []
            totalcount = Rehabilitation.objects.all().count()
            Cash_Compensation = Rehabilitation.objects.filter(compensationStatus='Cash Compensation').count()
            Land_Provided_Area = Rehabilitation.objects.filter(compensationStatus='Land Provided Area').count()
            Alternate_accommodation = Rehabilitation.objects.filter(compensationStatus='Alternate accommodation').count()
            Commercial_Unit = Rehabilitation.objects.filter(compensationStatus='Commercial Unit').count()
            Pending = Rehabilitation.objects.filter(compensationStatus='Pending').count()
            dataset.append(Cash_Compensation) , dataset.append( Land_Provided_Area) , 
            dataset.append(Alternate_accommodation) , dataset.append(Commercial_Unit) , dataset.append(Pending) 

            return Response({'status': 'success',
                            'Message': 'Data fetched successfully',
                            'dataset': dataset,
                            'totalcount': totalcount,
                            'Cash_Compensation' : Cash_Compensation ,
                            'Land_Provided_Area' : Land_Provided_Area,
                            'Alternate_accommodation' : Alternate_accommodation,
                            'Commercial_Unit' : Commercial_Unit,
                            'Pending': Pending ,
                                } , status= 200)
        except Exception:
            return Response({'Message': 'Something went wrong Please try again'} , status= 400)




class LabourCampFacilitiesDashboardView(GenericAPIView):
    serializer_class = LabourcampDashboardSerializer

    def get(self, request,labourCampName ,*args, **kwargs):
        dataset = []
        try:
            labour = LabourCamp.objects.filter(labourCampName = labourCampName).latest('id')
            data = LabourcampDashboardSerializer(labour).data
            values=list(data.values())
            dataset.append(values.count('Good')) ,dataset.append(values.count('Average'))
            dataset.append(values.count('Bad'))

            return Response({'status': 'success',
                            'Message': 'data Fetched successfully',
                            'dataset':dataset ,
                            'data' : data}, status=200)
        except:
            return Response({'status': 'error',
                            'Message': 'Something went wrong'},status=400)


    
        
            