
from .serializer import ( AirSerializer ,WaterSerializer,NoiseSerializer , TreeManagmentviewserializer,
TreeManagementSerailizer, Noiseviewserializer, WasteTreatmentsSerializer , MaterialSourcingSerializer ,AirViewSerializer,
waterviewserializer , wastetreatmentsViewserializer , MaterialSourcingViewserializer)
from rest_framework.response import Response
from .models import *
from rest_framework import generics
from .renderers import ErrorRenderer
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from django.contrib.gis.geos import Point,GEOSGeometry
from rest_framework.permissions import IsAuthenticated  , DjangoModelPermissions
from .paginations import LimitsetPagination
from Auth.permissions import IsConsultant , IsMMRDA
from .serializer import *


# class EnvMonitoringView(generics.GenericAPIView):
#     renderer_classes = [ErrorRenderer]
#     serializer_class = envMonitoringSerailzer
#     parser_classes = [MultiPartParser]
#     permission_classes = [IsAuthenticated]
    
#     def post(self, request):
#         serializer = envMonitoringSerailzer(data = request.data)
#         if serializer.is_valid(raise_exception= True):
#             serializer.save()
#             return Response(serializer.data , status = 200)
#         else:
#             return Response({'msg' :'Please enter valid data'} , status = 400 )

class AirView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    serializer_class = AirSerializer
    parser_classes = [MultiPartParser]
    # permission_classes = [ IsAuthenticated ,IsMMRDA]
    queryset = Air.objects.all()

    def post(self , request):
        lat=float(request.data['latitude'])
        long=float(request.data['longitude'])
        location=Point(long,lat,srid=4326)
        Serializer = AirSerializer(data = request.data)
        if Serializer.is_valid(raise_exception = True):
            air=Serializer.save(location=location)
            data=AirViewSerializer(air).data
            return Response(data, status= status.HTTP_200_OK)
        else:
            return Response(Serializer.errors , status= status.HTTP_400_BAD_REQUEST)


class AirListView(generics.ListAPIView):
    renderer_classes = [ErrorRenderer]
    pagination_class = LimitsetPagination 
    serializer_class = AirViewSerializer
    parser_classes = [MultiPartParser]
    queryset = Air.objects.all()


class WaterView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    serializer_class = WaterSerializer
    parser_classes = [MultiPartParser]
    queryset = water.objects.all()
    

    def post(self , request):
        lat=float(request.data['latitude'])
        long=float(request.data['longitude'])
        location=Point(long,lat,srid=4326)
        serializer = WaterSerializer(data = request.data )
        if serializer.is_valid(raise_exception = True):
            water_data =serializer.save(location=location)
            data = waterviewserializer(water_data).data

            return Response(data , status = 200)
        else:
            return Response({'msg' : 'Enter a valid data'} , status = 400)
class waterListView(generics.ListAPIView):
    serializer_class = waterviewserializer
    pagination_class = LimitsetPagination
    renderer_classes = [ErrorRenderer]
    queryset = water.objects.all()

class NoiseView(generics.GenericAPIView):
    renderer_classes = [ErrorRenderer]
    queryset = Noise.objects.all()
    serializer_class = NoiseSerializer
    parser_classes = [MultiPartParser]
    
    def post (self , request ):
        try:
            lat=float(request.data['latitude'])
            long=float(request.data['longitude'])
            location=Point(long,lat,srid=4326)
            serializer = NoiseSerializer(data = request.data )
            if serializer.is_valid(raise_exception= True):
                Noise  = serializer.save(location = location)
                data = Noiseviewserializer(Noise).data
                return Response (data , status = 200)
        except:
            return Response({'msg': 'Please Enter Valid data'} ,  status=400 )

class NoiseListView(generics.ListAPIView):
    pagination_class = LimitsetPagination
    serializer_class = Noiseviewserializer
    renderer_classes = [ErrorRenderer]
    queryset = Noise.objects.all()



class TreeManagementView(generics.GenericAPIView):
    serializer_class = TreeManagementSerailizer
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    queryset = TreeManagment.objects.all()
    # permission_classes = (DjangoModelPermissions , )

    def post(self , request):
        # if request.data['dateOfConduct'] == ''
        
        lat=float(request.data['latitude'])
        long=float(request.data['longitude'])
        location=Point(long,lat,srid=4326)

        Clat = float(request.data['Clatitude'])
        Clong = float(request.data['Clongitude'])
        location = Point(Clat,Clong,srid=4326)
        serializer = TreeManagementSerailizer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            tree = serializer.save(location = location , Clocation = location )
            data = TreeManagmentviewserializer(tree).data 
            return Response(data , status = status.HTTP_200_OK)
        else:
            return Response({'message': serializer.errors} , satus = status.HTTP_400_BAD_REQUEST)

class TereeManagementView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = TreeManagmentviewserializer
    pagination_class = LimitsetPagination
    parser_classes = [MultiPartParser]
    queryset = TreeManagment.objects.all()


class WasteTreatmentsView(generics.GenericAPIView):
    serializer_class = WasteTreatmentsSerializer
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    # permission_classes = [ mmrdaPermissions , ]
    
    def post(self , request):
        longitude = float(request.data['waste_longitude'])
        latitude = float(request.data['waste_latitude'])
        waste_location=Point(longitude,latitude,srid=4326)
        
        lat=float(request.data['latitude'])
        long=float(request.data['longitude'])
        location=Point(long,lat,srid=4326)

        serializer = WasteTreatmentsSerializer(data = request.data)
        if serializer.is_valid(raise_exception= True):
            waste = serializer.save(wasteHandlingLocation = waste_location,location =location )
            data = wastetreatmentsViewserializer(waste).data
            return Response({'msg':'Success',
                            'data' : data} , status = 200)
        else:
            return Response({'msg' : 'Please Eneter a valid data' ,
                            'errors' : serializer.errors } ,
                            status = 400)

class MaterialSourcingView(generics.GenericAPIView):
    serializer_class = MaterialSourcingSerializer
    renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    # permission_classes = [IsAuthenticated]

    def post(self , request):
       
        lat=float(request.data['latitude'])
        long=float(request.data['longitude'])
        location=Point(long,lat,srid=4326)
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception= True):
            material = serializer.save(location=location)
            data = MaterialSourcingViewserializer(material).data 
            return Response(data , status = status.HTTP_200_OK)
        else:
            return Response ({'msg' : "Please eneter a valid data"} , status = status.HTTP_400_BAD_REQUEST)


class TotalenvMonitoringView(generics.ListAPIView):
    serializer_class = AirSerializer
    queryset = Air.objects.all()

    def get(self , request):
        # env = EnvQualityMonitoring.objects.prefetch_related('airs').get(id = 2)
    
        air = Air.objects.all()
        airSerialzier = AirSerializer(self.get_queryset() , many = True).data

        Water = water.objects.all()
        WaterSerializer = waterviewserializer(Water , many = True).data

        noise = Noise.objects.all()
        NoiseSerializer = Noiseviewserializer(noise , many = True).data

        wastage = WasteTreatments.objects.all()
        wastageSerializer = WasteTreatmentsSerializer(wastage, many=True).data

        material = MaterialSourcing.objects.all()
        materialSeializer = MaterialSourcingSerializer(material, many=True).data

        return Response ({'air' :airSerialzier , 'water' :WaterSerializer ,
                        'Noise': NoiseSerializer,'wastage':wastageSerializer,'material':materialSeializer} , status = status.HTTP_200_OK)



class TreemanagmentAPI(generics.GenericAPIView):
    serializer_class = TreemanagementSerializer
    def get(self, request,packages, *args, **kwargs):
            packages = packages
            instance = TreeManagment.objects.filter(packages__iexact=packages)
            if instance :
                serializer = TreemanagementSerializer(instance, many=True)
                return Response({'status': 200,'data': serializer.data,
                                   'message': 'successfully'})
            else:
                return Response({'status':403,'message':'invalid package'})

class AirAPI(generics.GenericAPIView):
    serializer_class = AirmanagementSerializer
    def get(self, request,packages, *args, **kwargs):
        instance = Air.objects.filter(packages__iexact=packages)
        if instance:
            serializer = AirmanagementSerializer(instance, many=True)
            return Response({'status': 200, 'data': serializer.data,
                                      'message': 'successfully'})
        else:
            return Response({'status': 403, 'message': 'invalid package'})


class NoiseAPI(generics.GenericAPIView):
    serializer_class = NoisemanagementSerializer
    def get(self, request,packages, *args, **kwargs):
        packages = packages
        instance = Noise.objects.filter(packages__iexact=packages)
        if instance:
            serializer = NoisemanagementSerializer(instance, many=True)
            return Response({'status': 200, 'data': serializer.data,
                                      'message': 'successfully'})
        else:
            return Response({'status': 403, 'message': 'invalid package'})

class WasteTreatmentsAPI(generics.GenericAPIView):
    serializer_class = WasteSerializer 
    def get(self, request,packages, *args, **kwargs):
        packages = packages
        instance = WasteTreatments.objects.filter(packages__iexact=packages).exists()
        if instance:
            serializer = WasteSerializer(instance, many=True)
            return Response({'status': 200, 'data': serializer.data,
                                      'message': 'successfully'})
        else:
            return Response({'status': 403, 'message': 'invalid package'})

class MaterialSourcingAPI(generics.GenericAPIView):
    serializer_class = MaterialSerializer
    def get(self, request,packages, *args, **kwargs):
        packages = packages
        instance = MaterialSourcing.objects.filter(packages__iexact=packages)
        if instance:
            serializer = MaterialSerializer(instance, many=True)
            return Response({'status': 200, 'data': serializer.data,
                                      'message': 'successfully'})
        else:
            return Response({'status':403,'message':'invalid package'})

class WatermanagmentAPI(generics.GenericAPIView):
    serializer_class = WatermanamentSerializer
    def get(self, request,packages, *args, **kwargs):
        packages = packages
        instance = water.objects.filter(packages__iexact=packages)
        if instance:
            serializer = WatermanamentSerializer(instance, many=True)
            return Response({'status': 200, 'data': serializer.data,
                                      'message': 'successfully'})
        else:
            return Response({'status': 403, 'message': 'invalid package'})

