from rest_framework import generics
from .serialzers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.contrib.gis.geos import Point , MultiLineString
from .models import traning, photographs
from .permission import IsConsultant
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.


class TraningView(generics.GenericAPIView):
    serializer_class = TraningSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def post(self, request):
        try:
            serializer = TraningSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=200)
        except:
            return Response({'Please Enetr a valid data'}, status=400)


class TrainingListView(generics.ListAPIView):
    serializer_class = TraningSerializer
    permission_classes = [IsAuthenticated, IsConsultant]
    queryset = traning.objects.all()


class TrainingupdateView(generics.UpdateAPIView):
    serializer_class = TraningSerializer
    parser_classes = [MultiPartParser]
    queryset = traning.objects.all()

    def update(self, request, pk, *args, **kwargs):
        try:
            instance = traning.objects.get(id=pk)
            serializer = TraningSerializer(
                instance, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        except:
            return Response({'Message': 'Matching Id DoesNotExist'})


class PhotographsView(generics.GenericAPIView):
    serializer_class = photographsSerializer
    permission_classes = [IsAuthenticated, IsConsultant]
    parser_classes = [MultiPartParser]

    def post(self, request):
        lat = float(request.data['latitude'])
        long = float(request.data['longitude'])
        location = Point(long, lat, srid=4326)
        serializer = photographsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            phototgraph = serializer.save(location=location)
            data = photographsViewSerializer(phototgraph).data
            return Response(data, status=200)
        else:
            return Response(serializer.errors, status=400)


class photographsListView(generics.ListAPIView):
    serializer_class = photographsSerializer
    permission_classes = [IsAuthenticated, IsConsultant]
    parser_classes = [MultiPartParser]
    queryset = photographs.objects.all()


class updatephotographview(generics.UpdateAPIView):
    serializer_class = photographsViewSerializer
    parser_classes = [MultiPartParser]
    queryset = photographs.objects.all()

    def update(self, request, pk, *args, **kwargs):
        try:
            instance = photographs.objects.get(id=pk)
            serializer = photographsViewSerializer(
                instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
        except:
            return Response({"message": "Matching id does not exist"})


class occupationalHealthSafety (generics.GenericAPIView):
    serializer_class = occupationalHealthSafetySerialziers
    parser_classes = [MultiPartParser]
    
    def post(self, request):
        lat = float(request.data['latitude'])
        long = float(request.data['longitude'])
        location = Point(long, lat, srid=4326)
        serializer = occupationalHealthSafetySerialziers(data = request.data )
        if serializer.is_valid(raise_exception=True):
            rehabilitation = serializer.save(location=location)
            data = occupationalHealthSafetyViewSerializer(rehabilitation).data
            return Response(data, status=200)
        else:
            return Response({"message": serializer.errors}, status=400)




# def modify_input_for_multiple_files(images):
#     dict = {}
#     dict['images'] = images
#     return dict

class ContactUsView(generics.GenericAPIView):
    serializer_class = ContactusSerializezr
    parser_classes = [MultiPartParser ]

    def post(self, request):
        lat = float(request.data['latitude'])
        long = float(request.data['longitude'])
        location = Point(long, lat, srid=4326)

        serializer = ContactusSerializezr(data = request.data)
        if serializer.is_valid(raise_exception=True):
            contactus = serializer.save(location=location )
            data = ContactusViewSerialzier(contactus).data
            return Response(data, status=200)
        else:
            return Response({"message": serializer.errors}, status=400)
        # except:
        #     return Response ({'Message' : 'No data found'} , status= 400)


class ContactusListView(generics.ListAPIView):
    queryset = Contactus.objects.all()
    serializer_class = ContactusViewSerialzier
    filter_backends = [filters.SearchFilter]
    search_fields = ['^name' , '^email']



