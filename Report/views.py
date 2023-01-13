from rest_framework.generics import GenericAPIView , ListAPIView
from .serializers import *
from SocialMonitoring.models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated


''' --------------------------Labour Camp Report View----------------------------'''

class LabourcampReportPackageView(ListAPIView):
    serializer_class = LabourcampReportSerializer
    parser_classes = [MultiPartParser]
  

    def get(self, request, packages, labourCampName ,*args, **kwargs):
        try:
            previous = LabourCamp.objects.filter(packages = packages  , labourCampName = labourCampName ).order_by('-id')[1:]
            latest = LabourCamp.objects.filter(packages = packages , labourCampName = labourCampName ).latest('id')
            previousData = self.serializer_class(previous, many = True).data
            latestData = self.serializer_class(latest).data
            return Response({'Previous': previousData  , 'latest' : latestData}, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({'Message' : 'There is no data available for this Package or Quarter'} , status= status.HTTP_400_BAD_REQUEST)



class LabourCampReportQuarterView(ListAPIView):

    serializer_class = LabourcampReportSerializer
    parser_classes = [MultiPartParser] 

    def get(self, request, quarter, labourCampName,*args, **kwarges):
        try: 
            previous = LabourCamp.objects.filter(quarter = quarter , labourCampName = labourCampName).order_by('-id')[1:]

            latest = LabourCamp.objects.filter(quarter = quarter, labourCampName = labourCampName ).latest('id')
            previousData = self.serializer_class(previous, many = True).data
            latestData = self.serializer_class(latest).data
            
            return Response({'Previous': previousData ,
                            'latest' : latestData},    
                            status=status.HTTP_200_OK)
        except:
            return Response({'Message': 'There is no data available for this Package or Quarter'} , status=400)

#----------------------------------------------------------------

class ConstructionCampReportPackageView(ListAPIView):
    serializer_class = ConstructionCampReportSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, packages, constructionSiteName ,*args, **kwargs):
        try:
            previous = ConstructionSiteDetails.objects.filter( packages = packages , constructionSiteName = constructionSiteName ).order_by('-id')[1:]
            latest = ConstructionSiteDetails.objects.filter(packages = packages  , constructionSiteName = constructionSiteName ).latest('id')
            previousData = ConstructionCampReportSerializer(previous, many = True)
            latestData = ConstructionCampReportSerializer(latest)

            return Response({'Previous': previousData.data  ,
                             'latest' : latestData.data},
                              status=status.HTTP_200_OK)

        except Exception:
            return Response({'Message' : 'There is no data available for the Package or Quarter'} , status= status.HTTP_400_BAD_REQUEST)

class ConstructionCampReportQuarterView(ListAPIView):
    serializer_class = ConstructionCampReportSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, quarter, constructionSiteName,*args, **kwargs):
        try:
            previous = ConstructionSiteDetails.objects.filter(quarter = quarter, constructionSiteName = constructionSiteName).order_by('-id')[1:]
            latest = latest = ConstructionSiteDetails.objects.filter(quarter = quarter  , constructionSiteName = constructionSiteName ).latest('id')
            previousData = ConstructionCampReportSerializer(previous, many = True)
            latestData = ConstructionCampReportSerializer(latest)

            return Response({'Previous': previousData.data  ,
                             'latest' : latestData.data},
                              status=status.HTTP_200_OK)
        except Exception:
            return Response({'Message' : 'There is no data available for the Package or Quarter'} , status= status.HTTP_400_BAD_REQUEST)



#-------------------------------------------------------------------------
class PAPReportPackageView(ListAPIView):
    serializer_class = PAPReportSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, packages,*args, **kwargs):
        try:
            data = PAP.objects.filter( packages = packages).order_by('-id') 
            if not data.exists():
                return Response({'Message' : 'No data Found'}, status= status.HTTP_400_BAD_REQUEST) 
            
            papdata = PAPReportSerializer(data, many = True).data
            return Response({'Message': 'Success', 
                            "PAP's": papdata},
                             status=status.HTTP_200_OK)
        except Exception:
            return Response({'Message' : 'There is no data available for the Package or Quarter'},
                             status= status.HTTP_400_BAD_REQUEST)


class PAPReportQuarterView(ListAPIView):
    serializer_class = PAPReportSerializer
    parser_classes = [MultiPartParser]

    def get(self , request , quarter):
        try:
            data = PAP.objects.filter(quarter = quarter).order_by('-id') 
            if not data.exists():
                return Response({'Message' : 'No data Found'}, status= status.HTTP_400_BAD_REQUEST) 
            papdata = PAPReportSerializer(data, many = True).data
            return Response({'Message': 'Success',
                            "PAP's": papdata},
                            status=status.HTTP_200_OK)
        except:
            return Response({'Message' : 'There is no data available for the Package or Quarter'},
                             status= status.HTTP_400_BAD_REQUEST)



#------------------------------------------------------------
class RehabilitationReportPackageView(ListAPIView):
    serializer_class = RehabilitationReportSerializer
    parser_classes = [MultiPartParser]


    def get(self, request, packages,*args, **kwargs):
        try:
            data = Rehabilitation.objects.filter( packages = packages ).order_by('-id')
            if not data.exists():
                return Response({'Message' : 'No data Found'}, status= status.HTTP_400_BAD_REQUEST)
            Rehabilitationdata = RehabilitationReportSerializer(data, many = True).data

            return Response({'Message': 'Success', 
                            "Rehabilated PAP's Quarter wise": Rehabilitationdata},
                             status=status.HTTP_200_OK)
        except Exception:
            return Response({'Message' : 'There is no data available for the Package or Quarter'},
                            status= status.HTTP_400_BAD_REQUEST)


class RehabilitationReportQuarterView(ListAPIView):
    serializer_class = RehabilitationReportSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, quarter,*args, **kwargs):
            try:
                data = Rehabilitation.objects.filter( quarter = quarter ).order_by('-id')
                if not data.exists():
                    return Response({'Message' : 'No data Found'}, status= status.HTTP_400_BAD_REQUEST)
                Rehabilitation_data = RehabilitationReportSerializer(data, many = True).data

                return Response({'Message': 'Success', 
                                "Rehabilated PAP's Quarter wise": Rehabilitation_data},
                                status=status.HTTP_200_OK)
            except Exception:
                return Response({'Message' : 'There is no data available for the Quarter'},
                                status= status.HTTP_400_BAD_REQUEST)





'''----------------------- Env Monitoring Report View------------------------------'''


class AirReportPackageView(ListAPIView):
    serializer_class = AirReportSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, packages, *args, **kwargs):
        try:
            data = Air.objects.filter(packages = packages).order_by('-id')
            if not data.exists():
                return Response({'Message' : 'No data Found'}, status= status.HTTP_400_BAD_REQUEST)
            
            airdata = AirReportSerializer(data, many = True).data
            return Response({'Message': 'Success', 
                            "Air data": airdata},
                            status=status.HTTP_200_OK)                 
        except:
            return Response({'Message' : 'There is no data available for the Quarter'},
                                status= status.HTTP_400_BAD_REQUEST)

class AirReportQuarterView(ListAPIView):
    serializer_class = AirReportSerializer
    permission_classes = [MultiPartParser]

    def get(self, request, quarter , month, *args, **kwargs):
        try:
            data = Air.objects.filter(quarter = quarter , dateOfMonitoring__month = month ).order_by('-id')
            if not data.exists():
                return Response({'Message' : 'No data Found'}, status= status.HTTP_400_BAD_REQUEST)
            
            airdata = AirReportSerializer(data, many = True).data
            return Response({'Message': 'Success', 
                            "Air data": airdata},
                            status=status.HTTP_200_OK)                 
        except:
            return Response({'Message' : 'There is no data available for the Quarter'},
                                status= status.HTTP_400_BAD_REQUEST)


class NoiseReportpackageView(ListAPIView):
    serializer_class = NoiseReportSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, packages, *args, **kwargs):
        try:
            data = Noise.objects.filter(packages = packages).order_by('-id')
            if not data.exists():
                return Response({'Message' : 'No data Found'}, status= status.HTTP_400_BAD_REQUEST)
            
            Noise_data = NoiseReportSerializer(data, many = True).data
            return Response({'Message': 'Success', 
                            "Noise data": Noise_data},
                            status=status.HTTP_200_OK)                 
        except:
            return Response({'Message' : 'There is no data available for the Package'},
                                status= status.HTTP_400_BAD_REQUEST)


class NoiseReportQuarterView(ListAPIView):
    serializer_class = NoiseReportSerializer
    parser_classes =   [MultiPartParser]

    def get(self, request, quarter ,year, *args, **kwargs):
        try:
            data = Noise.objects.filter(quarter = quarter , dateOfMonitoring__year = year ).order_by('-id')
            if not data.exists():
                return Response({'Message' : 'No data Found'}, status= status.HTTP_400_BAD_REQUEST)
            
            Noise_data = NoiseReportSerializer(data, many = True).data
            return Response({'Message': 'Success', 
                            "Noise data": Noise_data},
                            status=status.HTTP_200_OK)                 
        except:
            return Response({'Message' : 'There is no data available for the Quarter'},
                                status= status.HTTP_400_BAD_REQUEST)    



class waterReportPackageView(ListAPIView):
    serializer_class = waterReportSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, packages, *args, **kwargs):
        try:
            data = water.objects.filter(packages = packages).order_by('-id')
            if not data.exists():
                return Response({'Message' : 'No data Found'}, status= status.HTTP_400_BAD_REQUEST)
            
            water_data = waterReportSerializer(data, many = True).data
            return Response({'Message': 'Success', 
                            "water data": water_data},
                            status=status.HTTP_200_OK)                 
        except:
            return Response({'Message' : 'There is no data available for the Package'},
                                status= status.HTTP_400_BAD_REQUEST)

class waterReportQuarterView(ListAPIView):
    serializer_class = waterReportSerializer
    parser_classes =   [MultiPartParser]

    def get(self, request, quarter,year, *args, **kwargs):
        try:
            data = water.objects.filter(quarter = quarter, dateOfMonitoring__year = year ).order_by('-id')
            if not data.exists():
                return Response({'Message' : 'No data Found'}, status= status.HTTP_400_BAD_REQUEST)
                
            water_data = waterReportSerializer(data, many = True).data
            return Response({'Message': 'Success', 
                            "water data": water_data},
                            status=status.HTTP_200_OK)                 
        except:
            return Response({'Message' : 'There is no data available for the Quarter'},
                                status= status.HTTP_400_BAD_REQUEST)


class WasteTreatmentsPackageView(ListAPIView):
    serializer_class = wasteTreatmentsSerializer
    parser_classes = [MultiPartParser]  

    def get(self, request, packages, *args, **kwargs):
        try:
            data = WasteTreatments.objects.filter(packages = packages).order_by('-id')
            if not data.exists():
                return Response({'Message' : 'No data Found'}, status= status.HTTP_400_BAD_REQUEST)
            
            Waste_data = wasteTreatmentsSerializer(data, many = True).data
            return Response({'Message': 'Success', 
                            "waste Management data": Waste_data},
                            status=status.HTTP_200_OK)                 
        except:
            return Response({'Message' : 'There is no data available for the Package'},
                                status= status.HTTP_400_BAD_REQUEST)

class WasteTreatmentsQuarterView(ListAPIView):
    serializer_class = wasteTreatmentsSerializer
    parser_classes =   [MultiPartParser]
    
    def get(self, request, quarter,year, *args, **kwargs):
        try:
            data = WasteTreatments.objects.filter(quarter = quarter, dateOfMonitoring__year = year ).order_by('-id')
            if not data.exists():
                return Response({'Message' : 'No data Found'}, status= status.HTTP_400_BAD_REQUEST)
                
            Waste_data = wasteTreatmentsSerializer(data, many = True).data
            return Response({'Message': 'Success',
                             "waste Management data": Waste_data}, status= 200)

        except:
            return Response({'Message' : 'There is no data available for the Quarter'},
                                status= status.HTTP_400_BAD_REQUEST)  


    
class MaterialManagementReporetpackageView(ListAPIView):
    serializer_class = materialManagementSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, packages, *args, **kwargs):
        try:
            data = MaterialManegmanet.objects.filter(packages = packages).order_by('-id')
            if not data.exists():
                return Response({'Message' : 'No data Found'}, status= status.HTTP_400_BAD_REQUEST)
            
            Material_data = materialManagementSerializer(data, many = True).data
            return Response({'Message': 'Success', 
                            "Material Management data": Material_data},
                            status=status.HTTP_200_OK)                 
        except:
            return Response({'Message' : 'There is no data available for the Package'},
                                status= status.HTTP_400_BAD_REQUEST)

class MaterialManagementReporetQuarterView(ListAPIView):
    serializer_class = materialManagementSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, quarter,year, *args, **kwargs):
        try:
            data = MaterialManegmanet.objects.filter(quarter = quarter, dateOfMonitoring__year = year ).order_by('-id')
            if not data.exists():
                return Response({'Message' : 'No data Found'},
                                 status= status.HTTP_400_BAD_REQUEST)
                
            Material_data = materialManagementSerializer(data, many = True).data
            return Response({'Message': 'Success',
                             "material Management data": Material_data},
                             status= 200)
        except:
            return Response({'Message' : 'There is no data available for the Quarter'},
                            status= status.HTTP_400_BAD_REQUEST)  