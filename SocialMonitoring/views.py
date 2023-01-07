from .serializers import (labourCampDetailSerializer,labourCampDetailviewSerializer,labourCampDetailGetviewSerializer,
PapSerailzer,papviewserialzer,ConstructionSiteDetailsViewSerializer, constructionSiteSerializer, LabourCampserializer,
LabourCampDetailSerializer, LabourCampDetailViewSerializer,RehabilitationViewSerializer,RehabilitationSerializer,PapUpdateSerialzier
 , PAPSerializer ,ConstructionSiteDetailsserializer  , LabourCampUpdateSerialzier)
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated 
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .renderers import ErrorRenderer
from django.contrib.gis.geos import Point 
from .models import    PAP  , ConstructionSiteDetails , LabourCamp , labourcampDetails , Rehabilitation
from .paginations import LimitsetPagination
from .permissions import *


#---------------Labour camp Serializer for GEO jason Format--------------------------------
class labourCampdetails(generics.GenericAPIView):
    serializer_class = labourCampDetailSerializer
    parser_classes = (MultiPartParser, )
    queryset =  labourcampDetails.objects.all()
    def post(self, request):
    
        lat = float(request.data['latitude'])
        long = float(request.data['longitude'])
        location = Point(long, lat, srid=4326)
        serializer = labourCampDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            pap = serializer.save(location=location)
            data = labourCampDetailviewSerializer(pap).data
            return Response(data, status=200)
        else:
            return Response({"msg": serializer.errors}, status=400)

class labourCampdetailsView(generics.GenericAPIView):
    serializer_class = labourCampDetailGetviewSerializer
    parser_classes = [MultiPartParser]
   
    def get(self, request,LabourCampName, *args, **kwargs):
      
        details = labourcampDetails.objects.filter(LabourCampName = LabourCampName)
        serializer = labourCampDetailGetviewSerializer(details, many=True)
        return Response(serializer.data, status=200)



#---------------------------- PAP View--------------------------------------------------
class PapView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    serializer_class = PapSerailzer
    permission_classes = [IsAuthenticated , IsRNR]
    parser_classes = [MultiPartParser]

    def post(self, request):
    
        lat = float(request.data['latitude'])
        long = float(request.data['longitude'])
        location = Point(long, lat, srid=4326)
        papid= request.data['PAPID']
        print(papid)
        try:
            if "RNR" in request.user.groups.values_list("name",flat=True):
                data = PAP.objects.filter(PAPID = papid).exists()
                print(data)
                if data == True:
                    return Response({'Message':'already data filled for this PAP'} , status=400)
                else:
                    serializer = PapSerailzer(data=request.data , context={'request': request} )
                    if serializer.is_valid(raise_exception=True):
                        pap = serializer.save(location=location)
                        data = papviewserialzer(pap).data
                        return Response(data, status=200)
                    else:
                        return Response({"msg": serializer.errors}, status=400)
        except:
            return Response({"Message": "You are not Authourize person to fill this Details"}, status=400)
            

class papupdateView(generics.UpdateAPIView):
    serializer_class = PapUpdateSerialzier
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    permission_classes=[IsAuthenticated,IsRNR]
    queryset = PAP.objects.all()

    def update(self, request , id ,  **kwargs):
        try:
            instance = PAP.objects.get(PAPID=id,user=request.user.id)
        except Exception:
            return Response({"msg": "There is no PAP data for user %s" % (request.user.username)})

        serializer = PapUpdateSerialzier(instance , data=request.data , partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": "Please Enter a valid data"})

class PapListView(generics.ListAPIView):
    serializer_class = papviewserialzer 
    permission_classes = [IsAuthenticated]
    queryset = PAP.objects.all()



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
            if "RNR" in request.user.groups.values_list("name",flat = True):
                data = Rehabilitation.objects.filter(PAPID = papid).exists()
                if data == True:
                    return Response({'Message':'already data filled for this PAP'}, status=400)
                else:
                    serializer = RehabilitationSerializer(data = request.data  , context={'request': request})
                    print(serializer.context)
                    if serializer.is_valid():
                        rehabilitation = serializer.save(location=location  )
                        data = RehabilitationViewSerializer(rehabilitation).data
                        return Response(data, status=200)
                    else:
                        return Response({"Message": serializer.errors}, status=400)
        except Exception:
            return Response({"Message": "You are not Authourize person to fill this Details"}, status=401)

            

#----------------------------- Labour Camp details View --------------------------------
class LabourCampDetailsView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated & (IsConsultant | IsContractor)]
    serializer_class = LabourCampDetailSerializer
    queryset = LabourCamp.objects.all()

    def post(self, request):
        lat = float(request.data['latitude'])
        long = float(request.data['longitude'])
        location = Point(long, lat, srid=4326)
        date=request.data['dateOfMonitoring'].split('-')
        quarter = request.data['quarter']
        try:
            if "contractor" in request.user.groups.values_list("name",flat=True):
                data = LabourCamp.objects.filter(quarter = quarter, dateOfMonitoring__year = int(date[0])).exists()
                if data == True:
                    return Response({'message':'already data filled for this Quarter'} , status=400)
                else:
                    serializer = LabourCampDetailSerializer(data=request.data , context={'request': request})
                    if serializer.is_valid(raise_exception=True):
                        LabourCampDetails = serializer.save(location=location)
                        data = LabourCampDetailViewSerializer(LabourCampDetails).data
                        return Response(data, status=200)
                    else:
                        return Response({
                            'msg' : "Please enter a valid data", 'error':serializer.errors ,'Status' : 400})
            else:
                serializer = LabourCampDetailSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    LabourCampDetails = serializer.save(location=location)
                    data = LabourCampDetailViewSerializer(LabourCampDetails).data
                    return Response(data, status=200)
                else:
                    return Response({
                        'msg' : "Please enter a valid data", 'error':serializer.errors ,'Status' : 400})
        except Exception:
            return Response({"msg": "Only consultant and contractor can fill this form"}, status=400)
            
class labourCampUpdateView(generics.UpdateAPIView):
    serializer_class = LabourCampUpdateSerialzier
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    permission_classes=[IsAuthenticated , IsConsultant]

    def update(self, request , id ,  **kwargs):
        try:
            instance = LabourCamp.objects.get(id=id, user=request.user.id)
        except Exception:
            return Response({"msg": "There is no labour Camp data for user %s" % (request.user.username)})

        serializer = LabourCampUpdateSerialzier(instance , data=request.data , partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": "Please Enter a valid data"})

# ------------------------------------ Construction site View 
class constructionSiteView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    serializer_class = constructionSiteSerializer

    def post(self, request):
       
        lat = float(request.data['latitude'])
        long = float(request.data['longitude'])
        location = Point(long, lat, srid=4326)
        constructionSiteID = request.data['constructionSiteID']
        constructionSiteName = request.data['constructionSiteName']
        try:
            if "contractor" in request.user.groups.values_list("name",flat = True ):
                data = ConstructionSiteDetails.objects.filter(constructionSiteID=constructionSiteID , constructionSiteName = constructionSiteName).exists()
                if data == True:
                    return Response({'message':'already data filled for this Construction Site'}, status=400)
                else:
                    serialzier = constructionSiteSerializer(data=request.data , context={'request': request})
                    if serialzier.is_valid(raise_exception=True):
                        construction = serialzier.save(location=location)
                        data = ConstructionSiteDetailsViewSerializer(construction).data
                        return Response(data, status=200)
                    else:
                        return Response({'msg': 'Please Enter a valid data'})
            else:
                serialzier = constructionSiteSerializer(data=request.data , context={'request': request})
                if serialzier.is_valid(raise_exception=True):
                    construction = serialzier.save(location=location)
                    data = ConstructionSiteDetailsViewSerializer(construction).data
                    return Response(data, status=200)
                else:
                    return Response({'msg': 'Please Enter a valid data'})
        except Exception:
            return Response({"msg": "Only consultant and contractor can fill this form"}, status=401)


class ConstructionSiteUpdateView(generics.GenericAPIView):
    serializer_class = constructionSiteSerializer
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    permission_classes=[IsAuthenticated , IsConsultant]

    def update(self, request , id ,  **kwargs):
        try:
            instance = ConstructionSiteDetails.objects.get(id=id, user=request.user.id)
        except Exception:
            return Response({"msg": "There is no Construction site data for user %s" % (request.user.username)})

        serializer = constructionSiteSerializer(instance , data=request.data , partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": "Please Enter a valid data"})

class ConstructionSiteListView(generics.ListAPIView):
    serializer_class = constructionSiteSerializer
    queryset = ConstructionSiteDetails.objects.all()





class PAPmanagmentAPI(generics.GenericAPIView):
    serializer_class = PAPSerializer
    def get(self, request,packages, *args, **kwargs):
            packages = packages
            instance = PAP.objects.filter(packages__iexact = packages)
            if instance:
                print('instance---------',instance)
                serializer = PAPSerializer(instance,many=True)
                return Response({'status': 200, 'data': serializer.data,
                                          'message': 'successfully'})
            else:
                return Response({'status':403,'message':'invalid package'})





class ConstructionSitemanagment(generics.GenericAPIView):
    serializer_class = ConstructionSiteDetailsserializer
    def get(self, request,packages, *args, **kwargs):
        packages = packages
        instance = ConstructionSiteDetails.objects.filter(packages__iexact = packages)
        print('instance-------------------',instance)
        if instance:
            serializer = ConstructionSiteDetailsserializer(instance, many=True)
            return Response({'status': 200, 'data': serializer.data,
                                      'message': 'successfully'})
        else:
            return Response({'status':403,'message':'invalid package'})


class LabourCampManagmentAPI(generics.GenericAPIView):
    serializer_class = LabourCampserializer
    def get(self, request,packages, *args, **kwargs):
        packages = packages
        instance = LabourCamp.objects.filter(packages__iexact = packages)
        if instance:
            serializer = LabourCampserializer(instance, many=True)
            return Response({'status': 200, 'data': serializer.data,
                                      'message': 'successfully'})
        else:
            return Response({'status':403,'message':'invalid package'})



