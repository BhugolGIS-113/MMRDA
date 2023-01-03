from .serializers import (PapSerailzer,papviewserialzer,ConstructionSiteDetailsViewSerializer, constructionSiteSerializer, LabourCampserializer,
                        LabourCampDetailSerializer, LabourCampDetailViewSerializer,RehabilitationViewSerializer,RehabilitationSerializer,PapUpdateSerialzier , PAPSerializer ,ConstructionSiteDetailsserializer )
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .renderers import ErrorRenderer
from django.contrib.gis.geos import Point, GEOSGeometry
from .models import    PAP  , ConstructionSiteDetails , LabourCamp
from .paginations import LimitsetPagination


class PapView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    serializer_class = PapSerailzer
    # permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def post(self, request):
    
        lat = float(request.data['latitude'])
        long = float(request.data['longitude'])
        location = Point(long, lat, srid=4326)
        serializer = PapSerailzer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            pap = serializer.save(location=location)
            data = papviewserialzer(pap).data
            return Response(data, status=200)
        else:
            return Response({"msg": serializer.errors}, status=400)

            
class papupdateView(generics.UpdateAPIView):
    serializer_class = PapUpdateSerialzier
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    queryset = PAP.objects.all()

    def update(self, request , id ,  **kwargs):
        instance = PAP.objects.get(id=id)
        serializer = PapUpdateSerialzier(instance , data=request.data , partial = True).data
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer)
        else:
            return Response({"msg": "Please Enter a valid data"})

class PapListView(generics.ListAPIView):
    serializer_class = papviewserialzer 
    permission_classes = [IsAuthenticated]
    queryset = PAP.objects.all()


class RehabilitationView(generics.GenericAPIView):
    serializer_class = RehabilitationSerializer
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        lat = float(request.data['latitude'])
        long = float(request.data['longitude'])
        location = Point(long, lat, srid=4326)
        serializer = RehabilitationSerializer(data = request.data )
        if serializer.is_valid(raise_exception=True):
            rehabilitation = serializer.save(location=location)
            data = RehabilitationViewSerializer(rehabilitation).data
            return Response(data, status=200)
        else:
            return Response({"msg": serializer.errors}, status=400)


class LabourCampDetailsView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    # permission_classes = [IsAuthenticated]
    serializer_class = LabourCampDetailSerializer
    queryset = LabourCamp.objects.all()

    def post(self, request):
        lat = float(request.data['latitude'])
        long = float(request.data['longitude'])
        location = Point(long, lat, srid=4326)
        serializer = LabourCampDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            LabourCampDetails = serializer.save(location=location)
            data = LabourCampDetailViewSerializer(LabourCampDetails).data
            return Response(data, status=200)
        else:
            return Response({
                'msg' : "Please enter a valid data",
                'error':serializer.errors ,
                'Status' : 400})



class constructionSiteView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    # permission_classes = [IsAuthenticated]
    serializer_class = constructionSiteSerializer

    def post(self, request):
       
        lat = float(request.data['latitude'])
        long = float(request.data['longitude'])
        location = Point(long, lat, srid=4326)
        serialzier = constructionSiteSerializer(data=request.data)
        if serialzier.is_valid(raise_exception=True):
            construction = serialzier.save(location=location)
            data = ConstructionSiteDetailsViewSerializer(construction).data
            return Response(data, status=200)
        else:
            return Response({'msg': 'Please Enter a valid data'})

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



