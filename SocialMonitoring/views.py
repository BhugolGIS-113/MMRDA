from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .renderers import ErrorRenderer
from django.contrib.gis.geos import Point
from .models import *
from .paginations import LimitsetPagination
from .permissions import *
from rest_framework import status
from rest_framework import filters

# ---------------Labour camp Serializer for GEO jason Format--------------------------------

class labourCampdetails(generics.GenericAPIView):
    serializer_class = labourCampDetailSerializer
    parser_classes = (MultiPartParser, )
    queryset = labourcampDetails.objects.all()

    def post(self, request):
        lat = float(request.data['latitude'])
        long = float(request.data['longitude'])
        location = Point(long, lat, srid=4326)
        try:
            serializer = labourCampDetailSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                pap = serializer.save(location=location)
                data = labourCampDetailviewSerializer(pap).data
                return Response({'status': 'success',
                                'Message': 'Data saved successfully',
                                 'data': data}, status=status.HTTP_200_OK)
            else:
                return Response({"Message": 'Something Went Wrong , Please Check all the details',
                                'status': 'failed'}, status=400)
        except:
            return Response({'status': 'failed',
                            'Message': 'Something Went Wrong'}, status=400)


class labourCampdetailsView(generics.ListAPIView):
    queryset = labourcampDetails.objects.all()
    serializer_class = labourCampDetailGetviewSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['LabourCampName' ,'LabourCampID']



# ---------------------------- PAP View--------------------------------------------------
class PapView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    serializer_class = PapSerailzer
    permission_classes = [IsAuthenticated, IsRNR]
    parser_classes = [MultiPartParser]

    def post(self, request):
        
        lat = float(request.data['latitude'])
        long = float(request.data['longitude'])
        location = Point(long, lat, srid=4326)
        papid = request.data['PAPID']
        try:
            if "RNR" in request.user.groups.values_list("name", flat=True):
                data = PAP.objects.filter(PAPID=papid).exists()
                if data == True:
                    return Response({'Message': 'already data filled for this PAP-ID',
                                    'status' : 'success'}, status=400)
                else:
                    serializer = PapSerailzer(
                        data=request.data, context={'request': request})
                    if serializer.is_valid(raise_exception=True):
                        pap = serializer.save(location=location, user=request.user)
                        data = papviewserialzer(pap).data
                        return Response ({'Message': 'data saved successfully',
                                        'status' : 'success'}, status=200)
                    else:
                        return Response({"Message": 'data Invalid please Try Again',
                                          'status' : 'failed'  }, status=400)
        except:
            return Response({"Message": "You are not Authourize person to fill this Details" ,
                             'status' : 'failed' }, status=401)


class papupdateView(generics.UpdateAPIView):
    serializer_class = PapUpdateSerialzier
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated, IsRNR]
    queryset = PAP.objects.all()

    def update(self, request, id,  **kwargs):
        try:
            instance = PAP.objects.get(PAPID=id, user=request.user.id)
        except Exception:
            return Response({"msg": "There is no PAP data for user %s" % (request.user.username)})

        serializer = PapUpdateSerialzier(
            instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"Message": "Please Enter a valid data"})


class PapListView(generics.ListAPIView):
    serializer_class = papviewserialzer
    permission_classes = [IsAuthenticated]
    queryset = PAP.objects.all()


class RehabilatedPAPIDView(generics.GenericAPIView):
    serializer_class = RehabilatedPAPIDSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, PAPID):
        try:
            papdata = PAP.objects.get(PAPID=PAPID)
        except:
            return Response({'Message': 'No data Avaialable for this PAPID',
                            'status' : 'success'}, status=200)
        serializers = RehabilatedPAPIDSerializer(papdata).data
        return Response(serializers, status=200)
        # except:
        #     return Response({'Message' : 'No data Avaialable for this   PAPID Exception'} , status =400)


# ------------------------------ Rehabilitation View ------------------------------
class RehabilitationView(generics.GenericAPIView):
    serializer_class = RehabilitationSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated, IsRNR]

    def post(self, request, *args, **kwargs):
        lat = float(request.data['latitude'])
        long = float(request.data['longitude'])
        location = Point(long, lat, srid=4326)
        papid = request.data['PAPID']
        try:
            if "RNR" in request.user.groups.values_list("name", flat=True):
                data = Rehabilitation.objects.filter(PAPID=papid).exists()
                if data == True:
                    return Response({'Message': 'already data filled for this PAP' ,
                                    'status' : 'success'}, status=400)
                else:
                    serializer = RehabilitationSerializer(
                        data=request.data )
                    print(serializer.context)
                    if serializer.is_valid():
                        rehabilitation = serializer.save(
                            location=location, user=request.user)
                        data = RehabilitationViewSerializer(
                            rehabilitation).data
                        return Response({'Message': 'data saved successfully',
                                        'status' : 'success'}, status=200)
                    else:
                        return Response({"Message": serializer.errors ,
                                        'status' : 'failed'}, status=400)
        except Exception:
            return Response({"Message": "You are not Authourize person to fill this Details" ,
                            'status' : 'failed'}, status=401)


# ----------------------------- Labour Camp details View --------------------------------

class LabourCampDetailsView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated & (IsConsultant | IsContractor)]
    parser_classes = [MultiPartParser]
    serializer_class = LabourCampDetailSerializer

    def post(self, request):
        lat = float(request.data['latitude'])
        long = float(request.data['longitude'])
        location = Point(long, lat, srid=4326)
        date = request.data['dateOfMonitoring'].split('-')
        quarter = request.data['quarter']
        try:
            if "contractor" in request.user.groups.values_list("name", flat=True):
                data = LabourCamp.objects.filter(
                    quarter=quarter, dateOfMonitoring__year=int(date[0])).exists()
                if data == True:
                    return Response({'Message': 'already data filled for this Quarter'}, status=400)
                else:
                    serializer = LabourCampDetailSerializer(data=request.data )
                    if serializer.is_valid(raise_exception=True):
                        LabourCampDetails = serializer.save(location=location , user = request.user)
                        data = LabourCampDetailViewSerializer(LabourCampDetails).data

                        return Response({'Message': 'data saved successfully',
                                        'status' : 'success'}, status=200)
                    else:
                        return Response({'Message': "Please enter a valid data", 
                                            'error': serializer.errors, 'Status': 'failed'}, status=400)
            else:
                serializer = LabourCampDetailSerializer(
                    data=request.data)
                if serializer.is_valid(raise_exception=True):
                    LabourCampDetails = serializer.save(location=location , user = request.user)
                    data = LabourCampDetailViewSerializer(
                        LabourCampDetails).data
                    return Response({'Message': 'data saved successfully',
                                     'status' : 'success'}, status=200)
                else:
                    return Response({'Message': "Please enter a valid data",
                                     'error': serializer.errors, 'Status': 'failed'} , status= 400)
        except Exception:
            return Response({"msg": "Only consultant and contractor can fill this form"}, status=401)


class labourCampUpdateView(generics.UpdateAPIView):
    serializer_class = LabourCampUpdateSerialzier
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated, IsConsultant]

    def update(self, request, id,  **kwargs):
        try:
            instance = LabourCamp.objects.get(id=id, user=request.user.id)
        except Exception:
            return Response({"msg": "There is no labour Camp data for user %s" % (request.user.username)})

        serializer = LabourCampUpdateSerialzier(
            instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Message': 'data saved successfully',
                                     'status' : 'success'}, status=200)
        else:
            return Response({'Message': "Please enter a valid data",
                            'error': serializer.errors, 'Status': 'failed'} , status= 400)

# ------------------------------------ Construction site View -----------------------------------------------------


class constructionSiteView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    serializer_class = constructionSiteSerializer

    def post(self, request):

        lat = float(request.data['latitude'])
        long = float(request.data['longitude'])
        location = Point(long, lat, srid=4326)
        constructionSiteId = request.data['constructionSiteId']
        constructionSiteName = request.data['constructionSiteName']
        try:
            if "contractor" in request.user.groups.values_list("name", flat=True):
                data = ConstructionSiteDetails.objects.filter(
                    constructionSiteId=constructionSiteId, constructionSiteName=constructionSiteName).exists()
                if data == True:
                    return Response({'message': 'already data filled for this Construction Site',
                                    'status': 'success'}, status=400)
                else:
                    serialzier = constructionSiteSerializer(
                        data=request.data, context={'request': request})
                    if serialzier.is_valid(raise_exception=True):
                        construction = serialzier.save(location=location , user = request.user)
                        data = ConstructionSiteDetailsViewSerializer(
                            construction).data
                        return  Response({'Message': 'data saved successfully',
                                     'status' : 'success'}, status=200)
                    else:
                        return Response({'Message': "Please enter a valid data",
                                         'Status': 'failed'} , status= 400)
            else:
                serialzier = constructionSiteSerializer(
                    data=request.data, context={'request': request})
                if serialzier.is_valid(raise_exception=True):
                    construction = serialzier.save(location=location , user = request.user)
                    data = ConstructionSiteDetailsViewSerializer(
                        construction).data
                    return  Response({'Message': 'data saved successfully',
                                     'status' : 'success'}, status=200)
                else:
                    return Response({'Message': "Please enter a valid data",
                                         'Status': 'failed'} , status= 400)
        except Exception:
            return Response({"msg": "Only consultant and contractor can fill this form"}, status=401)


class ConstructionSiteUpdateView(generics.GenericAPIView):
    serializer_class = constructionSiteSerializer
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated, IsConsultant]

    def update(self, request, id,  **kwargs):
        try:
            instance = ConstructionSiteDetails.objects.get(
                id=id, user=request.user.id)
        except Exception:
            return Response({"Message": "There is no Construction site data for user %s" % (request.user.username),
                            'status': 'success'} , status=200)

        serializer = constructionSiteSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Message': 'data updated successfully',
                            'status' : 'success'}, status=200)
        else:
            return Response({"Message": "Please Enter a valid data" ,
                            'status' : 'failed'}, status= 400)


class ConstructionSiteListView(generics.ListAPIView):
    serializer_class = constructionSiteSerializer
    queryset = ConstructionSiteDetails.objects.all()


class PAPmanagmentAPI(generics.GenericAPIView):
    serializer_class = PAPSerializer

    def get(self, request, packages, *args, **kwargs):
        packages = packages
        instance = PAP.objects.filter(packages__iexact=packages)
        if instance:
            serializer = PAPSerializer(instance, many=True)
            return Response({'Message': 'data updated successfully',
                            'status' : 'success'}, status=200)
        else:
            return Response({'status': 'failed',
                             'Message': 'invalid package'} , status= 400)


class ConstructionSitemanagment(generics.GenericAPIView):
    serializer_class = ConstructionSiteDetailsserializer

    def get(self, request, packages, *args, **kwargs):
        packages = packages
        instance = ConstructionSiteDetails.objects.filter(
            packages__iexact=packages)
        if instance:
            serializer = ConstructionSiteDetailsserializer(instance, many=True)
            return Response({'status': 'success', 'data': serializer.data,
                             'Message': 'successfully'} , status = 200)
        else:
            return Response({'status': 'failed', 'Message': 'invalid package'} , status =  400)


class LabourCampManagmentAPI(generics.GenericAPIView):
    serializer_class = LabourCampserializer

    def get(self, request, packages, *args, **kwargs):
        packages = packages
        instance = LabourCamp.objects.filter(packages__iexact=packages)
        if instance:
            serializer = LabourCampserializer(instance, many=True)
            return Response({'status': 'success', 'data': serializer.data,
                             'Message': 'successfully'} , status=200)
        else:
            return Response({'status': 'failed', 'Message': 'invalid package'}, status= 400)
