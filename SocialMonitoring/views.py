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
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

# ---------------Labour camp Serializer for GEO jason Format--------------------------------

# The above class is a view for creating and saving post-labour camp details with latitude and
# longitude coordinates.
class PostlabourCampdetails(generics.GenericAPIView):
    serializer_class = labourCampDetailSerializer
    parser_classes = (MultiPartParser, )
    queryset = labourcampDetails.objects.all()

    def post(self, request):
        
        try:
            serializer = labourCampDetailSerializer(data=request.data)
            if serializer.is_valid():
                lat = float(serializer.validated_data['latitude'])
                long = float(serializer.validated_data['longitude'])
                location = Point(long, lat, srid=4326)
                pap = serializer.save(location=location)
                data = labourCampDetailviewSerializer(pap).data
                return Response({'status': 'success',
                                'Message': 'Data saved successfully',
                                 'data': data}, status=status.HTTP_200_OK)
            else:
                key, value =list(serializer.errors.items())[0]
                error_message = key+" ,"+value[0]
                return Response({'status': 'error',
                                'Message' :value[0]} , status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'status': 'failed',
                            'Message': 'Something Went Wrong'}, status=400)


class labourCampdetailsView(generics.ListAPIView):
    queryset = labourcampDetails.objects.all()
    serializer_class = labourCampDetailGetviewSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['LabourCampName' ,'LabourCampID']


class labourCampdetailsViewSearch(generics.ListAPIView):
    queryset = labourcampDetails.objects.all()
    serializer_class = labourCampDetailGetviewSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['LabourCampName']




# ---------------------------- PAP View--------------------------------------------------
# The `PapView` class is a view in a Django REST framework API that handles the creation of a PAP
# (Personal Assistance Program) object, with different validation and permission checks based on the
# user's group.
class PapView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    serializer_class = PapSerailzer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def post(self, request):
        if "RNR" in request.user.groups.values_list("name", flat=True):
            serializer = PapSerailzer(data=request.data, context={'request': request})
            if serializer.is_valid():
                papid = serializer.validated_data["PAPID"]
                data = PAP.objects.filter(PAPID=papid).exists()
                if data == True:
                    return Response({'Message': 'already data filled for this PAP-ID',
                                    'status' : 'success'}, status=400)
                else:
                    lat = float(serializer.validated_data['latitude'])
                    long = float(serializer.validated_data['longitude'])
                    location = Point(long, lat, srid=4326)
                    pap = serializer.save(location=location, user=request.user)
                    data = papviewserialzer(pap).data
                    return Response ({'Message': 'data saved successfully',
                                    'status' : 'success' , 
                                    }, status=200)
            else:    
                key, value =list(serializer.errors.items())[0]
                error_message = key+" ,"+value[0]
                print(error_message)
                return Response({'status': 'error',
                                'Message' :error_message} , status = status.HTTP_400_BAD_REQUEST)
            
        elif "consultant" in request.user.groups.values_list("name" , flat = True):
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                lat = float(serializer.validated_data['latitude'])
                long = float(serializer.validated_data['longitude'])
                location = Point(long, lat, srid=4326)
                pap = serializer.save(location=location , user = request.user)
                data = papviewserialzer(pap).data 
                return Response ({'Message': 'data saved successfully',
                                    'status' : 'success'}, status=200)
            else:
                key, value =list(serializer.errors.items())[0]
                error_message = key+" ,"+value[0]
                print(error_message)
                return Response({'status': 'error',
                                'Message' :error_message} , status = status.HTTP_400_BAD_REQUEST)
        else:
        # except Exception:
            return Response({"msg": "Only consultant and contractor can fill this form"}, status=401)

        
# The `papupdateView` class is a view in a Django REST framework API that handles updating a PAP
# object with partial data.
class papupdateView(generics.UpdateAPIView):
    serializer_class = PapUpdateSerialzier
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    def update(self, request, id,  **kwargs):
        try:
            instance = PAP.objects.get(PAPID=id, user=request.user.id)
        except Exception:
            return Response({"message": "There is no PAP data for user %s" % (request.user.username)})

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
        for i in serializers.values():
            if i == "Not agreed":
                return Response ({"status": "error" , 
                              "message" : "Person with this PAP-ID is not agreed for rehabilitaion"} , status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializers, status=200)
        

# ------------------------------ Rehabilitation View ------------------------------
# The `RehabilitationView` class is a view in a Django REST framework API that handles the creation of
# rehabilitation data, with different validation and permission checks based on the user's group.
class RehabilitationView(generics.GenericAPIView):
    serializer_class = RehabilitationSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
     
        
        if "RNR" in request.user.groups.values_list("name", flat=True):
            serializer = RehabilitationSerializer(data=request.data )
            if serializer.is_valid():
                papid = serializer.validated_data['PAPID']
                data = Rehabilitation.objects.filter(PAPID=papid).exists()
                if data == True:
                    return Response({'Message': 'already data filled for this PAP' ,
                                    'status' : 'success'})
                else:
                    lat = float(serializer.validated_data['latitude'])
                    long = float(serializer.validated_data['longitude'])
                    location = Point(long, lat, srid=4326)
                    rehabilitation = serializer.save(location=location, user=request.user)
                    data = RehabilitationViewSerializer(rehabilitation).data
                    return Response({'Message': 'data saved successfully',
                                    'status' : 'success'})
            else:
                key, value =list(serializer.errors.items())[0]
                error_message = key+" ,"+value[0]
                return Response({'status': 'error',
                                'Message' :error_message} , status = status.HTTP_400_BAD_REQUEST)

        elif "consultant" in request.user.groups.values_list("name" , flat = True):
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                lat = float(serializer.validated_data['latitude'])
                long = float(serializer.validated_data['longitude'])
                location = Point(long, lat, srid=4326)
                rehabilitation = serializer.save(location=location , user = request.user)
                data = RehabilitationViewSerializer(rehabilitation).data
                return Response({'Message': 'data saved successfully',
                                    'status' : 'success'})
            else:
                key, value =list(serializer.errors.items())[0]
                error_message = key+" ,"+value[0]
                return Response({'status': 'error',
                                'Message' :error_message} , status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"msg": "Only consultant and contractor can fill this form"}, status=401)


# ----------------------------- Labour Camp details View --------------------------------

# The `LabourCampDetailsView` class is a view in a Django REST framework API that allows authenticated
# users who are either consultants or contractors to submit data for a labour camp, with different
# validation and response logic based on the user's role.
class LabourCampDetailsView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated & (IsConsultant | IsContractor)]
    parser_classes = [FormParser]
    serializer_class = LabourCampDetailSerializer

    def post(self, request):
    
        if "contractor" in request.user.groups.values_list("name", flat=True):
            serializer = self.get_serializer(data=request.data )
            if serializer.is_valid():
                date = str(serializer.validated_data['dateOfMonitoringTwo']).split('-')
                quarter = serializer.validated_data['quarter']
                packages = serializer.validated_data["packages"]
                data = LabourCamp.objects.filter(quarter=quarter, dateOfMonitoring__year=int(date[0]) , packages = packages).exists()
                if data == True:
                    return Response({'Message': 'already data filled for this Quarter'}, status=400)
                else:
                    lat = float(serializer.validated_data['latitude'])
                    long = float(serializer.validated_data['longitude'])
                    location = Point(long, lat, srid=4326)

                    # toiletPhotograph = []
                    # drinkingWaterPhotographs = []
                    # demarkationOfPathwaysPhotographs = []

                    # file_mapping = {
                    #     'toiletPhotograph': toiletPhotograph,
                    #     'drinkingWaterPhotographs': drinkingWaterPhotographs,
                    #     'demarkationOfPathwaysPhotographs' : demarkationOfPathwaysPhotographs,
                    # }
                    # for field in ['toiletPhotograph', 'drinkingWaterPhotographs' , 'demarkationOfPathwaysPhotographs', 'signagesLabelingPhotographs',
                    #       'kitchenAreaPhotographs' ,'roomsOrDomsPhotographs' , 'fireExtinguishPhotographs' ,
                    #       'segregationOfWastePhotographs' , 'regularHealthCheckupPhotographs' , 'availabilityOfDoctorPhotographs' , 
                    #       'firstAidKitPhotographs' , 'photographs' , 'documents']:
                
                    #     files = request.FILES.getlist(field)
                    #     if files is not None:
                    #         for file in files:
                    #             tmp = os.path.join(settings.MEDIA_ROOT, 'contactus/images/', file.name)

                    #             path = default_storage.save(tmp, ContentFile(file.read()))
                    #             tmp_file = os.path.join(settings.MEDIA_ROOT, path)
                                
                    #             file_list = file_mapping.get(field)
                    #             if file_list is not None:
                    #                 file_list.append('/media/contactus/images/' + file.name)

                    LabourCampDetails = serializer.save(location=location , user = request.user)
                    data = LabourCampDetailViewSerializer(LabourCampDetails).data

                    return Response({'Message': 'data saved successfully',
                                    'status' : 'success'}, status=200)
            else:
                key, value =list(serializer.errors.items())[0]
                error_message = key+" ,"+value[0]
                return Response({'status': 'error',
                                'Message' :error_message} , status = status.HTTP_400_BAD_REQUEST)
            
        elif "consultant" in request.user.groups.values_list("name" , flat = True):
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                lat = float(serializer.validated_data['latitude'])
                long = float(serializer.validated_data['longitude'])
                location = Point(long, lat, srid=4326)
                LabourCampDetails = serializer.save(location=location , user = request.user)
                data = LabourCampDetailViewSerializer(LabourCampDetails).data
                return Response({'Message': 'data saved successfully',
                                    'status' : 'success'}, status=200)
            else:
                key, value =list(serializer.errors.items())[0]
                error_message = key+" ,"+value[0]
                return Response({'status': 'error',
                                'Message' :error_message} , status = status.HTTP_400_BAD_REQUEST)
        else:
        # except Exception:
            return Response({"msg": "Only consultant and contractor can fill this form"}, status=401)


# The `labourCampUpdateView` class is a view in a Django REST framework API that allows authenticated
# consultants to update labour camp data.
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


# The `constructionSiteView` class is a view in a Django REST framework API that handles the creation
# of construction site data, with different validation and permission checks based on the user's role.
class constructionSiteView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    serializer_class = constructionSiteSerializer

    def post(self, request):
        if "contractor" in request.user.groups.values_list("name", flat=True):
            serialzier = constructionSiteSerializer( data=request.data, context={'request': request})
            if serialzier.is_valid():
                constructionSiteId = serialzier.validated_data['constructionSiteId']
                constructionSiteName = serialzier.validated_data['constructionSiteName']
                data = ConstructionSiteDetails.objects.filter(constructionSiteId = constructionSiteId, constructionSiteName=constructionSiteName).exists()
                if data == True:
                    return Response({'message': 'already data filled for this Construction Site',
                                    'status': 'success'}, status=400)
                else:
                    lat = float(serialzier.validated_data['latitude'])
                    long = float(serialzier.validated_data['longitude'])
                    location = Point(long, lat, srid=4326)
                    construction = serialzier.save(location=location , user = request.user)
                    data = ConstructionSiteDetailsViewSerializer(
                        construction).data
                    return  Response({'Message': 'data saved successfully',
                                'status' : 'success'}, status=200)
            else:
                key, value =list(serialzier.errors.items())[0]
                error_message = key+" ,"+value[0]
                return Response({'status': 'error',
                                'Message' :error_message} , status = status.HTTP_400_BAD_REQUEST)
        elif "consultant" in request.user.groups.values_list("name", flat=True):
            serialzier = constructionSiteSerializer( data=request.data, context={'request': request})
            if serialzier.is_valid(raise_exception=True):
                lat = float(serialzier.validated_data['latitude'])
                long = float(serialzier.validated_data['longitude'])
                location = Point(long, lat, srid=4326)
                construction = serialzier.save(location=location , user = request.user)
                data = ConstructionSiteDetailsViewSerializer(
                    construction).data
                return  Response({'Message': 'data saved successfully',
                                    'status' : 'success'}, status=200)
            else:
                key, value =list(serialzier.errors.items())[0]
                error_message = key+" ,"+value[0]
                return Response({'status': 'error',
                                    'Message' :error_message} , status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"msg": "Only consultant and contractor can fill this form"}, status=401)


# The ConstructionSiteUpdateView class is a view in a Python Django application that handles updating
# construction site data.
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


