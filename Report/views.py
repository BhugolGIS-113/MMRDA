from rest_framework.generics import ListAPIView
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

    def get(self, request, packages, labourCampName, *args, **kwargs):
        try:
            previous = LabourCamp.objects.filter(
                packages=packages, labourCampName=labourCampName).order_by('-id')[1:]
            latest = LabourCamp.objects.filter(
                packages=packages, labourCampName=labourCampName).latest('id')
            previousData = self.serializer_class(previous, many=True)
            latestData = self.serializer_class(latest)

            return Response({'Message': 'data Fetched Successfully',
                            'status' : 'success' , 
                            'Previous': previousData.data,
                             'latest': latestData.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'Message': 'There is no data available for this Package or Quarter',
                            'status' : 'Failed'}, status=status.HTTP_400_BAD_REQUEST)


class LabourCampReportQuarterView(ListAPIView):

    serializer_class = LabourcampReportSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, quarter, labourCampName, year, *args, **kwarges):
        try:
            previous = LabourCamp.objects.filter(
                quarter=quarter, labourCampName=labourCampName, dateOfMonitoring__year=year).order_by('-id')[1:]

            latest = LabourCamp.objects.filter(
                quarter=quarter, labourCampName=labourCampName).latest('id')
            previousData = self.serializer_class(previous, many=True).data
            latestData = self.serializer_class(latest).data

            return Response({'Message': 'data Fetched Successfully',
                            'status' : 'success' , 
                            'Previous': previousData,
                            'latest': latestData},
                            status=status.HTTP_200_OK)
        except:
            return Response({'Message': 'There is no data available for this Package or Quarter',
                            'status' : 'Failed'}, status=400)

# ----------------------------------------------------------------


class ConstructionCampReportPackageView(ListAPIView):
    serializer_class = ConstructionCampReportSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, packages, constructionSiteName, *args, **kwargs):
        try:
            previous = ConstructionSiteDetails.objects.filter(
                packages=packages, constructionSiteName=constructionSiteName).order_by('-id')[1:]
            latest = ConstructionSiteDetails.objects.filter(
                packages=packages, constructionSiteName=constructionSiteName).latest('id')
            previousData = ConstructionCampReportSerializer(
                previous, many=True)
            latestData = ConstructionCampReportSerializer(latest)

            return Response({'Message': 'data Fetched Successfully',
                            'status' : 'success' , 
                            'Previous': previousData.data,
                            'latest': latestData.data},
                            status=status.HTTP_200_OK)

        except Exception:
            return Response({'Message': 'There is no data available for the Package or Quarter',
                            'status' : 'Failed'}, status=status.HTTP_400_BAD_REQUEST)


class ConstructionCampReportQuarterView(ListAPIView):
    serializer_class = ConstructionCampReportSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, quarter, constructionSiteName, *args, **kwargs):
        try:
            previous = ConstructionSiteDetails.objects.filter(
                quarter=quarter, constructionSiteName=constructionSiteName).order_by('-id')[1:]
            latest = latest = ConstructionSiteDetails.objects.filter(
                quarter=quarter, constructionSiteName=constructionSiteName).latest('id')
            previousData = ConstructionCampReportSerializer(
                previous, many=True)
            latestData = ConstructionCampReportSerializer(latest)

            return Response({'Message': 'data Fetched Successfully',
                            'status' : 'success' , 
                            'Previous': previousData.data,
                            'latest': latestData.data},
                            status=status.HTTP_200_OK)
        except Exception:
            return Response({'Message': 'There is no data available for the Package or Quarter',
                            'status' : 'Failed'}, status=status.HTTP_400_BAD_REQUEST)

# -------------------------------------------------------------------------


class PAPReportPackageView(ListAPIView):
    serializer_class = PAPReportSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, packages, *args, **kwargs):
        try:
            data = PAP.objects.filter(packages=packages).order_by('-id')
            if not data.exists():
                return Response({'Message': 'No data found',
                                 'status' : 'success'},  status=status.HTTP_200_OK)
            papdata = PAPReportSerializer(data, many=True).data
            return Response({'Message': 'data Fetched Successfully',
                            'status' : 'success' , 
                            "PAP": papdata},
                            status=status.HTTP_200_OK)
        except Exception:
            return Response({'Message': 'There is no data available for the Package or Quarter',
                            'status' : 'Failed'},
                            status=status.HTTP_400_BAD_REQUEST)


class PAPReportQuarterView(ListAPIView):
    serializer_class = PAPReportSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, quarter, year):
        try:
            data = PAP.objects.filter(
                quarter=quarter, dateOfMonitoring__year=year).order_by('-id')
            if not data.exists():
                return Response({'Message': 'No data found',
                                 'status' : 'success'},  status=status.HTTP_200_OK)
            papdata = PAPReportSerializer(data, many=True).data
            return Response({'Message': 'data Fetched Successfully',
                            'status' : 'success' , 
                            "PAP": papdata},
                            status=status.HTTP_200_OK)
        except:
            return Response({'Message': 'There is no data available for the Package or Quarter',
                            'status' : 'Failed'},
                            status=status.HTTP_400_BAD_REQUEST)


# ------------------------------------------------------------
class RehabilitationReportPackageView(ListAPIView):
    serializer_class = RehabilitationReportSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, packages, *args, **kwargs):
        try:
            data = Rehabilitation.objects.filter(
                packages=packages).order_by('-id')
            if not data.exists():
                return Response({'Message': 'No data found',
                                 'status' : 'success'},  status=status.HTTP_200_OK)
            Rehabilitationdata = RehabilitationReportSerializer(
                data, many=True).data

            return Response({'Message': 'data Fetched Successfully',
                            'status' : 'success' , 
                            "Rehabilated_PAP_Package": Rehabilitationdata},
                            status=status.HTTP_200_OK)
        except Exception:
            return Response({'Message': 'There is no data available for the Package or Quarter',
                            'status' : 'Failed'},
                            status=status.HTTP_400_BAD_REQUEST)


class RehabilitationReportQuarterView(ListAPIView):
    serializer_class = RehabilitationReportSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, quarter, year, *args, **kwargs):
        try:
            data = Rehabilitation.objects.filter(
                quarter=quarter, dateOfRehabilitation__year=year).order_by('-id')
            if not data.exists():
                return Response({'Message': 'No data found',
                                 'status' : 'success'},  status=status.HTTP_200_OK)
            Rehabilitation_data = RehabilitationReportSerializer(
                data, many=True).data

            return Response({'Message': 'data Fetched Successfully',
                            'status' : 'success' , 
                            "Rehabilated_PAP_Quarter_wise": Rehabilitation_data},
                            status=status.HTTP_200_OK)
        except Exception:
            return Response({'Message': 'There is no data available for the Quarter',
                            'status' : 'Failed'},
                            status=status.HTTP_400_BAD_REQUEST)


'''----------------------- Env Monitoring Report View------------------------------'''


class AirReportPackageView(ListAPIView):
    serializer_class = AirReportSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, packages, *args, **kwargs):
        try:
            data = Air.objects.filter(packages=packages).order_by('-id')
            if not data.exists():
                return Response({'Message': 'No data found',
                                 'status' : 'success'},  status=status.HTTP_200_OK)
            airdata = AirReportSerializer(data, many=True).data
            return Response({'Message': 'data Fetched Successfully',
                            'status' : 'success' , 
                            "Air_data": airdata},
                            status=status.HTTP_200_OK)
        except:
            return Response({'Message': 'There is no data available for the Quarter',
                            'status' : 'Failed'},
                            status=status.HTTP_400_BAD_REQUEST)


class AirReportQuarterView(ListAPIView):
    serializer_class = AirReportSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, month, year, *args, **kwargs):
        try:
            data = Air.objects.filter(
                month=month, dateOfMonitoring__year=year).order_by('-id')
            if not data.exists():
                return Response({'Message': 'No data found',
                                 'status' : 'success'},  status=status.HTTP_200_OK)

            airdata = AirReportSerializer(data, many=True).data
            return Response({'Message': 'data Fetched Successfully',
                            'status' : 'success' , 
                            "Air_data": airdata},
                            status=status.HTTP_200_OK)
        except:
            return Response({'Message': 'There is no data available for the Quarter',
                            'status' : 'Failed'},
                            status=status.HTTP_400_BAD_REQUEST)


class NoiseReportpackageView(ListAPIView):
    serializer_class = NoiseReportSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, packages, *args, **kwargs):
        try:
            data = Noise.objects.filter(packages=packages).order_by('-id')
            if not data.exists():
                return Response({'Message': 'No data found',
                                 'status' : 'success'},  status=status.HTTP_200_OK)

            Noise_data = NoiseReportSerializer(data, many=True).data
            return Response({'Message': 'data Fetched Successfully',
                            'status' : 'success' , 
                            "Noise_data": Noise_data},
                            status=status.HTTP_200_OK)
        except:
            return Response({'Message': 'There is no data available for the Package',
                            'status' : 'Failed'},
                            status=status.HTTP_400_BAD_REQUEST)


class NoiseReportQuarterView(ListAPIView):
    serializer_class = NoiseReportSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, quarter, year, *args, **kwargs):
        try:
            data = Noise.objects.filter(
                quarter=quarter, dateOfMonitoring__year=year).order_by('-id')
            if not data.exists():
                return Response({'Message': 'No data found',
                                 'status' : 'success'},  status=status.HTTP_200_OK)

            Noise_data = NoiseReportSerializer(data, many=True).data
            return Response({'Message': 'data Fetched Successfully',
                            'status' : 'success' , 
                            "Noise data": Noise_data},
                            status=status.HTTP_200_OK)
        except:
            return Response({'Message': 'There is no data available for the Quarter',
                            'status' : 'Failed'},
                            status=status.HTTP_400_BAD_REQUEST)


class waterReportPackageView(ListAPIView):
    serializer_class = waterReportSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, packages, *args, **kwargs):
        try:
            data = water.objects.filter(packages=packages).order_by('-id')
            if not data.exists():
                return Response({'Message': 'No data found',
                                 'status' : 'success'},  status=status.HTTP_200_OK)

            water_data = waterReportSerializer(data, many=True).data
            return Response({'Message': 'data Fetched Successfully',
                            'status' : 'success' , 
                            "water_data": water_data}, status=status.HTTP_200_OK)
        except:
            return Response({'Message': 'There is no data available for the Package',
                            'status' : 'Failed'},
                            status=status.HTTP_400_BAD_REQUEST)


class waterReportQuarterView(ListAPIView):
    serializer_class = waterReportSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, quarter, year, *args, **kwargs):
        try:
            data = water.objects.filter(
                quarter=quarter, dateOfMonitoring__year=year).order_by('-id')
            if not data.exists():
                return Response({'Message': 'No data found',
                                 'status' : 'success'},  status=status.HTTP_200_OK)

            water_data = waterReportSerializer(data, many=True).data
            return Response({'Message': 'data Fetched Successfully',
                            'status' : 'success' , 
                            "water_data": water_data},
                            status=status.HTTP_200_OK)
        except:
            return Response({'Message': 'There is no data available for the Quarter',
                            'status' : 'Failed'},
                            status=status.HTTP_400_BAD_REQUEST)


class WasteTreatmentsPackageView(ListAPIView):
    serializer_class = wasteTreatmentsSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, packages, *args, **kwargs):
        try:
            data = WasteTreatments.objects.filter(
                packages=packages).order_by('-id')
            if not data.exists():
                return Response({'Message': 'No data found',
                                 'status' : 'success'},  status=status.HTTP_200_OK)
            Waste_data = wasteTreatmentsSerializer(data, many=True).data

            return Response({'Message': 'data Fetched Successfully',
                            'status' : 'success' , 
                            "waste_Management data": Waste_data},
                            status=status.HTTP_200_OK)
        except:
            return Response({'Message': 'There is no data available for the Package',
                            'status' : 'Failed'},
                            status=status.HTTP_400_BAD_REQUEST)


class WasteTreatmentsQuarterView(ListAPIView):
    serializer_class = wasteTreatmentsSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, quarter, year, *args, **kwargs):
        try:
            data = WasteTreatments.objects.filter(
                quarter=quarter, dateOfMonitoring__year=year).order_by('-id')
            if not data.exists():
                return Response({'Message': 'No data found',
                                 'status' : 'success'},  status=status.HTTP_200_OK)

            Waste_data = wasteTreatmentsSerializer(data, many=True).data
            return Response({'Message': 'data Fetched Successfully',
                            'status' : 'success' , 
                             "waste_Management data": Waste_data}, status=200)

        except:
            return Response({'Message': 'There is no data available for the Quarter',
                            'status' : 'Failed'},
                            status=status.HTTP_400_BAD_REQUEST)


class MaterialManagementReporetpackageView(ListAPIView):
    serializer_class = materialManagementSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, packages, *args, **kwargs):
        try:
            data = MaterialManegmanet.objects.filter(
                packages=packages).order_by('-id')
            if not data.exists():
                return Response({'Message': 'No data found',
                                 'status' : 'success'},  status=status.HTTP_200_OK)

            Material_data = materialManagementSerializer(data, many=True).data
            return Response({'Message': 'data Fetched Successfully',
                            'status' : 'success' , 
                            "Material_Management_data": Material_data},
                            status=status.HTTP_200_OK)
        except:
            return Response({'Message': 'There is no data available for the Package',
                            'status' : 'Failed'},
                            status=status.HTTP_400_BAD_REQUEST)


class MaterialManagementReporetQuarterView(ListAPIView):
    serializer_class = materialManagementSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, quarter, year, *args, **kwargs):
        try:
            data = MaterialManegmanet.objects.filter(
                quarter=quarter, dateOfMonitoring__year=year).order_by('-id')
            if not data.exists():
                return Response({'Message': 'No data found',
                                 'status' : 'success'},  status=status.HTTP_200_OK)

            Material_data = materialManagementSerializer(data, many=True).data
            return Response({'Message': 'data Fetched Successfully',
                            'status' : 'success' , 
                             "material Management data": Material_data},
                            status=200)
        except:
            return Response({'Message': 'There is no data available for the Quarter',
                            'status' : 'Failed'},
                            status=status.HTTP_400_BAD_REQUEST)


class TreeMangementReportPackage(ListAPIView):
    serializer_class = treeManagementSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, packages, *args, **kwargs):
        try:
            data = TreeManagment.objects.filter(
                packages=packages).order_by('-id')
            if not data.exists():
                return Response({'Message': 'No data found',
                                 'status' : 'success'},  status=status.HTTP_200_OK)

            Material_data = treeManagementSerializer(data, many=True).data
            return Response({'Message': 'data Fetched Successfully',
                            'status' : 'success' , 
                            "Tree Management data": Material_data},
                            status=status.HTTP_200_OK)
        except:
            return Response({'Message': 'There is no data available for the Package',
                            'status' : 'Failed'},
                            status=status.HTTP_400_BAD_REQUEST)


class TreeManagementReportQuarterView(ListAPIView):
    serializer_class = treeManagementSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, quarter, year, *args, **kwargs):
        try:
            data = TreeManagment.objects.filter(
                quarter=quarter, dateOfMonitoring__year=year).order_by('-id')
            if not data.exists():
                return Response({'Message': 'No data found',
                                 'status' : 'success'},  status=status.HTTP_200_OK)

            Material_data = treeManagementSerializer(data, many=True).data
            return Response({'Message': 'data Fetched Successfully',
                            'status' : 'success' , 
                             "Tree Management data": Material_data},
                            status=200)
        except:
            return Response({'Message': 'There is no data available for the Quarter',
                            'status' : 'Failed'},
                            status=status.HTTP_400_BAD_REQUEST)
