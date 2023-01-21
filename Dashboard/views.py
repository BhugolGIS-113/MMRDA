from rest_framework.generics import GenericAPIView
from .serializers import *
from EnvMonitoring.models import *
from Training.models import *
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
                                'Residential' : Residential,
                                'Commercial' : Commercial,
                                'Private_Land':Private_Land,
                                'Government_Land' : Government_Land,
                                'Institutional' : Institutional,
                                'Other' : Other
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

class CashCompensationTypeCharView(GenericAPIView):

    def get(self, request):
        try:
            dataset = []
            Area = Rehabilitation.objects.filter(typeOfCompensation = '2.5 x Area').count()
            Cash = Rehabilitation.objects.filter(typeOfCompensation = 'Cash').count()
            Both = Rehabilitation.objects.filter(typeOfCompensation = 'Both').count()
            Pending = Rehabilitation.objects.filter(typeOfCompensation = 'Pending').count()
            dataset.append(Area) , dataset.append(Cash) , dataset.append(Both),dataset.append(Pending)

            return Response ({'status': 'success',
                                'Message': 'data fetched Successfully',
                                'dataset':dataset,
                                '2.5x_Area': Area,
                                'Cash':Cash,
                                'Both':Both,
                                'Pending':Pending} , status=200)
        except:
            return Response({'status': 'error',
                            'Message': 'Something went wrong'},status=400)



class ExistingTreeCount(GenericAPIView):
    serializer_class = ExistingTreeSerializer   
    def get(self, request):
        try:
            ExistingTreeCount = []
            NewtreeCount = []
            treecount = ExistingTreeManagment.objects.all().count()
            NewTreeCount = NewTreeManagement.objects.all().count()
            ExistingTreeCount.append(treecount) , NewtreeCount.append(NewTreeCount)
            return Response({'status': 'success',
                            'Message': 'Data was successfully fetched',
                            'ExistingTreeCount': ExistingTreeCount,
                            'NewtreeCount' : NewtreeCount ,
                            },status=200)
        except:
            return Response({'status': 'error',
                            'Message': 'Something went wrong'},status=400)

                    


class WasteTypeCount(APIView):
    
    def get(self, request):
        try:
            dataset = []
            Hazardous_Waste = WasteTreatments.objects.filter(wastetype = 'Hazardous Waste').count()
            Bio_Waste = WasteTreatments.objects.filter(wastetype = 'Bio Waste').count()
            Electrical_Waste = WasteTreatments.objects.filter(wastetype = 'Electrical Waste').count()
            Non_Bio_Waste = WasteTreatments.objects.filter(wastetype = 'Non-Bio Waste').count()
            dataset.append(Hazardous_Waste) , dataset.append(Bio_Waste) , dataset.append(Electrical_Waste)
            dataset.append(Non_Bio_Waste)

            return Response ({'status': 'success',
                            'Message': 'Data was successfully fetched',
                            'dataset': dataset ,
                            'Hazardous_Waste' : Hazardous_Waste,
                            'Bio_Waste' : Bio_Waste ,
                            'Electrical_Waste' : Electrical_Waste,
                            'Non_Bio_Waste' : Non_Bio_Waste}, status= 200)
        except:
            return Response({'status': 'error',
                            'Message': 'Something went wrong'},status=400)

class WasteHandelingChart(APIView):
    def get(self, request):
        try:
            dataset = []
            Disposal = WasteTreatments.objects.filter(wastehandling = 'Disposal').count()
            Dump = WasteTreatments.objects.filter(wastehandling = 'Dump').count()
            Transportation = WasteTreatments.objects.filter(wastehandling = 'Transportation').count()
            Recycling = WasteTreatments.objects.filter(wastehandling = 'Recycling').count()

            dataset.append(Disposal) , dataset.append(Dump) , dataset.append(Transportation) , dataset.append(Recycling)
            return Response ({'status': 'success',
                                'Message': 'Data was successfully fetched',
                                'dataset': dataset ,
                                'Disposal' : Disposal,
                                'Dump' : Dump,
                                'Transportation' : Transportation,
                                'Recycling' : Recycling},status=200)
        except:
            return Response({'status': 'error',
                            'Message': 'Something went wrong'},status=400)


class MaterialSourceTypeCountChart(APIView):
    
    def get(self, request):
        try:
            dataset = []
            quarry = MaterialManegmanet.objects.filter(source = 'Quarry').count()
            Factory = MaterialManegmanet.objects.filter(source = 'Factory').count()
            Casting_Yard = MaterialManegmanet.objects.filter(source = 'Casting Yard').count()
            Local_Vendor = MaterialManegmanet.objects.filter(source = 'Local Vendor').count()
            Others = MaterialManegmanet.objects.filter(source = 'Others').count()
            dataset.append(quarry) , dataset.append(Factory) , dataset.append(Casting_Yard)
            dataset.append(Local_Vendor) , dataset.append(Others)

            return Response ({'status': 'success',
                                'Message': 'Data was successfully fetched',
                                'dataset': dataset ,
                                'quarry' : quarry, 'Factory' : Factory,
                                'Casting_Yard' : Casting_Yard , 'Local_Vendor' : Local_Vendor,
                                'Others' : Others} , status=200)
        except:
            return Response({'status': 'error',
                            'Message': 'Something went wrong'},status=400)

class MaterialConditionChart(APIView):
    def get(self, request):
        try:
            dataset = []
            Safe = MaterialManegmanet.objects.filter(materialstorageCondition = 'Safe').count()
            Unsafe = MaterialManegmanet.objects.filter(materialstorageCondition = 'Unsafe').count()
            Need_Improvement = MaterialManegmanet.objects.filter(materialstorageCondition = 'Need Improvement').count()
            dataset.append(Safe) , dataset.append(Unsafe) ,dataset.append(Need_Improvement)


            return Response ({'status': 'success',
                            'Message': 'Data was successfully fetched',
                            'dataset' : dataset,
                            'Safe' : Safe,
                            'Unsafe' : Unsafe ,
                            'Need_Improvement' : Need_Improvement }, status= 200)
        except:
            return Response({'status': 'error',
                            'Message': 'Something went wrong'},status=400)
        
            
class IncidenttypeCountchart(APIView):

    def get(self, request):
        dataset = []
        Reportable_Accident = occupationalHealthSafety.objects.filter(typeOfIncident='Reportable Accident').count()
        Reportable_NonFatal_Accident = occupationalHealthSafety.objects.filter(typeOfIncident= 'Reportable Non-Fatal Accident').count()
        First_Aid_Cases = occupationalHealthSafety.objects.filter(typeOfIncident= 'First Aid Cases').count()
        Dangerous_Occurrences = occupationalHealthSafety.objects.filter(typeOfIncident= 'Dangerous Occurrences').count()
        Man_Days_lost = occupationalHealthSafety.objects.filter(typeOfIncident= 'Man Days Lost').count()
        Major_Road_accident = occupationalHealthSafety.objects.filter(typeOfIncident= 'Major (Road accident)').count()
        Road_Incident = occupationalHealthSafety.objects.filter(typeOfIncident= 'Road Incident').count()
        Tree_Broken = occupationalHealthSafety.objects.filter(typeOfIncident= 'Tree Broken').count()
        Natural_Death = occupationalHealthSafety.objects.filter(typeOfIncident= 'Natural Death').count()
        Third_Party_Incident = occupationalHealthSafety.objects.filter(typeOfIncident= '3rd Party Incident').count()
        dataset.append(Reportable_Accident) , dataset.append(Reportable_NonFatal_Accident) , dataset.append(First_Aid_Cases)
        dataset.append(Dangerous_Occurrences) , dataset.append(Man_Days_lost),dataset.append(Major_Road_accident)
        dataset.append(Road_Incident),dataset.append(Tree_Broken) , dataset.append(Natural_Death) , dataset.append(Third_Party_Incident)

        return Response({'status': 'success',
                            'Message': 'Data was successfully fetched',
                            'dataset' : dataset,} , status= 200)
                            












          
        



    
        
            