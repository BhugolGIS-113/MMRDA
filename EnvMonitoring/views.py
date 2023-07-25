
from .serializer import *
from rest_framework.response import Response
from .models import *
from rest_framework import generics
# from .renderers import ErrorRenderer
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from django.contrib.gis.geos import Point,GEOSGeometry
from rest_framework.permissions import IsAuthenticated  , DjangoModelPermissions
from .paginations import LimitsetPagination
from Auth.permissions import IsConsultant , IsMMRDA
from .serializer import *
from .permissions import IsConsultant , IsContractor




class AirView(generics.GenericAPIView):
    # renderer_classes = [ErrorRenderer]
    serializer_class = AirSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [ IsAuthenticated & (IsConsultant | IsContractor)]
    queryset = Air.objects.all()

    def post(self , request):
        # try:
            if "contractor" in request.user.groups.values_list("name",flat=True):
                Serializer = self.get_serializer(data = request.data , context={'request': request})
                if Serializer.is_valid():
                    date = str(Serializer.validated_data['dateOfMonitoringTwo']).split('-')
                    month  = Serializer.validated_data['month']
                    data = Air.objects.filter( dateOfMonitoring__year = int(date[0]) , month = month , user = request.user.id).exists()
                    if data == True:
                        return Response({'status': 'success',
                                        'message':'already data filled for this Month'} , status=400)
                    else:
                        lat=float(Serializer.validated_data['latitude'])
                        long=float(Serializer.validated_data['longitude'])
                        location=Point(long,lat,srid=4326)
                        air=Serializer.save(location=location ,  user = request.user)
                        data=AirViewSerializer(air).data
                        return Response({'status': 'success',
                                        'message' : 'data saved successfully',
                                        'data': data}, status= status.HTTP_200_OK)
                else:
                    key, value =list(Serializer.errors.items())[0]
                    error_message = key+" ,"+value[0]
                    print(value[0])
                    return Response({'status' : 'error',
                                    'message' : value[0]}, status = 400)
            else:
                Serializer = AirSerializer(data = request.data , context={'request': request})
                if Serializer.is_valid():
                    lat=float(Serializer.validated_data['latitude'])
                    long=float(Serializer.validated_data['longitude'])
                    location=Point(long,lat,srid=4326)
                    air=Serializer.save(location=location , user = request.user)
                    data=AirViewSerializer(air).data
                    return Response({'status': 'success',
                                        'message' : 'data saved successfully',
                                        'data': data}, status= status.HTTP_200_OK)
                else:
                    key, value =list(Serializer.errors.items())[0]
                    error_message = key+" ,"+value[0]
                    print(value[0])
                    return Response({'status' : 'failed',
                                    'message' : value[0]}, status = 400)
        # except Exception:
        #     return  Response({'status' : 'failed',
        #                     'message' : "Only consultant and Contractor can fill this form"}, status=400)

class AirUpdateView(generics.UpdateAPIView):
    serializer_class = AirSerializer
    # renderer_classes = [ErrorRenderer]
    permission_classes = [IsAuthenticated , IsConsultant]
    parser_classes = [MultiPartParser]

    def update(self, request , id ,  **kwargs):
        try:
            instance = Air.objects.get(id=id,user=request.user.id)
        except Exception:
            return Response({'success' : 'success' , 
                            "message": "There is no Air data for user %s" % (request.user.username)})

        serializer = AirSerializer(instance , data=request.data , partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'success' : 'success' ,
                            'message' : 'Data Updated Successfully'} , status= 200)
        else:
            return Response({'status' : 'failed' , 
                            "message": "Please Enter a valid data"} , status= 400)

class AirListView(generics.ListAPIView):
 
    serializer_class = AirViewSerializer
    parser_classes = [MultiPartParser]
    queryset = Air.objects.all()



class WaterView(generics.GenericAPIView):
    # renderer_classes = [ErrorRenderer]
    serializer_class = WaterSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [ IsAuthenticated & (IsConsultant | IsContractor)]

    
    def post(self , request):
        # try:
        if "contractor" in request.user.groups.values_list("name",flat=True):
            serializer = WaterSerializer(data = request.data , context={'request': request})
            if serializer.is_valid():
                date = str(serializer.validated_data['dateOfMonitoringTwo']).split('-')
                quarter = serializer.validated_data['quarter']
                data = water.objects.filter( dateOfMonitoringTwo__year = int(date[0]) , quarter = quarter).exists()
                if data == True:
                    return Response({'status':'success' , 
                                    'Message': 'already data filled for this Quarter'} , status=status.HTTP_400_BAD_REQUEST)
                else:
                    lat=float(serializer.validated_data['latitude'])
                    long=float(serializer.validated_data['longitude'])
                    location=Point(long,lat,srid=4326)
                    water_data =serializer.save(location=location , user = request.user)
                    data = waterviewserializer(water_data).data
                    return Response({'status': 'success' , 
                                    'Message' : 'data saved successfully',
                                    'data' : data }, status = 200)
            else:
                key, value =list(serializer.errors.items())[0]
                error_message = key+" ,"+value[0]
                return Response({'status': 'error',
                                'Message' :value[0]} , status = status.HTTP_400_BAD_REQUEST)
        else:
        
            serializer = WaterSerializer(data = request.data , context={'request': request})
            if serializer.is_valid():
                lat=float(serializer.validated_data['latitude'])
                long=float(serializer.validated_data['longitude'])
                location=Point(long,lat,srid=4326)
                water_data =serializer.save(location=location , user = request.user)
                data = waterviewserializer(water_data).data
                return Response({'status': 'success' , 
                                    'Message' : 'data saved successfully',
                                    'datat' : data }, status = 200)
            else:
                key, value =list(serializer.errors.items())[0]
                error_message = key+" ,"+value[0]
                return Response({'status': 'failed',
                                'Message' : value[0]} , status = status.HTTP_400_BAD_REQUEST)
        # except Exception:
        #     return  Response({'status': 'failed',
        #                     'Message' : "Only consultant and Contractor can fill this form"}, status= status.HTTP_401_UNAUTHORIZED)


class waterupdateView(generics.UpdateAPIView):
    # renderer_classes = [ErrorRenderer]
    serializer_class = waterviewserializer
    permission_classes = [IsAuthenticated , IsConsultant]
    parser_classes = [MultiPartParser]

    def update(self, request , id , **kwargs):
        try:
            instance = water.objects.get(id=id,user=request.user.id)
        except Exception:
            return Response({'status' : 'success',
                            "Message": "There is no Water data for user %s" % (request.user.username)})
        serializer = AirSerializer(instance , data=request.data , partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'status': 'success' , 
                            'Message' : 'data saved successfully'}, status = 200)
        else:
            return Response({'status' : 'failed' , 
                            "Message": "Please Enter a valid data"} , status= 400)

class waterListView(generics.ListAPIView):
    serializer_class = waterviewserializer
    parser_classes = [MultiPartParser]
    pagination_class = LimitsetPagination
    # renderer_classes = [ErrorRenderer]
    queryset = water.objects.all()




class NoiseView(generics.GenericAPIView):
    # renderer_classes = [ErrorRenderer]
    serializer_class = NoiseSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [ IsAuthenticated & (IsConsultant | IsContractor)]
    
    def post(self , request):
        try:
            if "contractor" in request.user.groups.values_list("name",flat=True):
                serializer = NoiseSerializer(data = request.data , context={'request': request})
                if serializer.is_valid():
                    date = str(serializer.validated_data['dateOfMonitoringThree']).split('-')
                    month  = serializer.validated_data['month']
                    data = Noise.objects.filter( dateOfMonitoringThree__year = int(date[0]) , month = month).exists()
                    if data == True:
                        return Response({'status':'success' , 
                                        'Message': 'already data filled for this Month'} , status=status.HTTP_400_BAD_REQUEST)
                    else:
                        lat=float(serializer.validated_data['latitude'])
                        long=float(serializer.validated_data['longitude'])
                        location=Point(long,lat,srid=4326)
                        water_data =serializer.save(location=location , user = request.user)
                        data = Noiseviewserializer(water_data).data
                        return Response({'status': 'success' , 
                                        'Message' : 'data saved successfully',
                                        'data' : data }, status = 200)
                else:
                    key, value =list(serializer.errors.items())[0]
                    error_message = key+" ,"+value[0]
                    return Response({'status': 'failed',
                                    'Message' : value[0]} , status = status.HTTP_400_BAD_REQUEST)
            else:
                serializer = NoiseSerializer(data = request.data , context={'request': request})
                if serializer.is_valid():
                    lat=float(serializer.validated_data['latitude'])
                    long=float(serializer.validated_data['longitude'])
                    location=Point(long,lat,srid=4326)
                    water_data =serializer.save(location=location , user = request.user)
                    data = Noiseviewserializer(water_data).data
                    return Response({'status': 'success' , 
                                    'Message' : 'data saved successfully',
                                    'data' : data }, status = 200)
                else:
                    key, value =list(serializer.errors.items())[0]
                    error_message = key+" ,"+value[0]
                    return Response({'status': 'failed',
                                    'Message' : value[0]} , status = status.HTTP_400_BAD_REQUEST)
        except Exception:
            return  Response({'status': 'failed',
                            'Message' : "Only consultant and Contractor can fill this form"} , status= status.HTTP_401_UNAUTHORIZED)

class NoiseupdateView(generics.UpdateAPIView):
    serializer_class = NoiseSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated , IsConsultant]

    def update(self, request , id , **kwargs):
        try:
            instance = Noise.objects.get(id=id,user=request.user.id)
        except Exception:
            return Response({"Message": "There is no Noise data for user %s" % (request.user.username)})
        serializer = NoiseSerializer(instance , data=request.data , partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": "Please Enter a valid data"})
        

class NoiseListView(generics.ListAPIView):
    pagination_class = LimitsetPagination
    serializer_class = Noiseviewserializer
    # renderer_classes = [ErrorRenderer]
    queryset = Noise.objects.all()



class ExistingTreeManagementView(generics.GenericAPIView):
    serializer_class = TreeManagementSerailizer
    # renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    # permission_classes = [IsAuthenticated]
  
    
    def post(self , request):
        # try:
            if "contractor" in request.user.groups.values_list("name",flat=True):
                serializer = TreeManagementSerailizer(data = request.data )
                if serializer.is_valid():
                    date = str(serializer.validated_data['dateOfMonitoring']).split('-')
                    month  = serializer.validated_data['month']
                    data = ExistingTreeManagment.objects.filter( dateOfMonitoring__year = int(date[0]) , month = month ).exists()
                    if data == True:
                        return Response({'message':'already data filled for this Month'} , status=status.HTTP_400_BAD_REQUEST)
                    else:
                        lat=float(serializer.validated_data['latitude'])
                        long=float(serializer.validated_data['longitude'])
                        Plocation=Point(long,lat,srid=4326)
                        water_data =serializer.save(location=Plocation , user = request.user)
                        data = TreeManagmentviewserializer(water_data).data
                        return Response({'status': 'success' , 
                                        'Message' : 'data saved successfully',
                                        'data' : data }, status = 200)
                else:
                    key, value =list(serializer.errors.items())[0]
                    error_message = key+" ," + value[0]
                    return Response({'status': 'error',
                                    'Message' :value[0]} , status = status.HTTP_400_BAD_REQUEST)
            else:
                serializer = TreeManagementSerailizer(data = request.data )
                if serializer.is_valid():
                    lat=float(serializer.validated_data['latitude'])
                    long=float(serializer.validated_data['longitude'])
                    Plocation=Point(long,lat,srid=4326)
                    water_data =serializer.save(location=Plocation , user = request.user)
                    data = TreeManagmentviewserializer(water_data).data
                    return Response({'status': 'success' , 
                                        'Message' : 'data saved successfully',
                                        'data' : data }, status = 200)
                else:
                    key, value =list(serializer.errors.items())[0]
                    error_message = key+" ," + value[0]
                    return Response({'status': 'error',
                                    'Message' :value[0]} , status = status.HTTP_400_BAD_REQUEST)
        # except Exception:
        #     return  Response({'status': 'failed',
        #                     'Message' : "Only consultant and Contractor can fill this form"} , status= status.HTTP_401_UNAUTHORIZED)

            

class ExistingTreeManagmentUpdateView(generics.UpdateAPIView):
    serializer_class = TreeManagementSerailizer
    permission_classes = [IsAuthenticated, IsConsultant]
    
    def update(self, request , id , **kwargs):
        try:
            instance = ExistingTreeManagment.objects.get(id=id,user=request.user.id)
        except Exception:
            return Response({"msg": "There is no Tree data for user %s" % (request.user.username)})
        serializer = TreeManagementSerailizer(instance , data=request.data , partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": "Please Enter a valid data"})

            
class ExistingTereeManagementView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = TreeManagmentviewserializer
    pagination_class = LimitsetPagination
    # parser_classes = [MultiPartParser]
    queryset = ExistingTreeManagment.objects.all()



class NewTereeManagementView(generics.GenericAPIView):
    serializer_class = NewTreeManagmentSerializer
    parser_classes = [MultiPartParser]

    def post(self , request):
        
        lat=float(request.data['latitude'])
        long=float(request.data['longitude'])
        location=Point(long,lat,srid=4326)
        
        try:
            if "contractor" in request.user.groups.values_list("name",flat=True):
                serializer = NewTreeManagmentSerializer(data = request.data )
                if serializer.is_valid():
                    date = str(serializer.validated_data['dateOfMonitoring']).split('-')
                    month  = serializer.validated_data['month']
                    data = NewTreeManagement.objects.filter( dateOfMonitoring__year = int(date[0]) , month = month ).exists()
                    if data == True:
                        return Response({'message':'already data filled for this Month'} , status=status.HTTP_400_BAD_REQUEST)
                    else:
                        lat=float(serializer.validated_data['latitude'])
                        long=float(serializer.validated_data['longitude'])
                        location=Point(long,lat,srid=4326)
                        water_data =serializer.save(location=location , user = request.user)
                        data = NewTreeManagmentviewserializer(water_data).data
                        return Response({'status': 'success' , 
                                        'Message' : 'data saved successfully',
                                        'data' : data }, status = 200)
                else:
                    key, value =list(serializer.errors.items())[0]
                    error_message = key+" ," + value[0]
                    return Response({'status': 'error',
                                    'Message' :value[0]} , status = status.HTTP_400_BAD_REQUEST)
            else:
                serializer = NewTreeManagmentSerializer(data = request.data )
                if serializer.is_valid():
                    lat=float(serializer.validated_data['latitude'])
                    long=float(serializer.validated_data['longitude'])
                    location=Point(long,lat,srid=4326)
                    water_data =serializer.save(location=location , user = request.user)
                    data = NewTreeManagmentviewserializer(water_data).data
                    return Response({'status': 'success' , 
                                        'Message' : 'data saved successfully',
                                        'data' : data }, status = 200)
                else:
                    key, value =list(serializer.errors.items())[0]
                    error_message = key+" ," + value[0]
                    return Response({'status': 'error',
                                    'Message' :value[0]} , status = status.HTTP_400_BAD_REQUEST)
        except Exception:
            return  Response({'Message' : "Only consultant and Contractor can fill this form"}, status= status.HTTP_401_UNAUTHORIZED)


class WasteTreatmentsView(generics.GenericAPIView):
    serializer_class = WasteTreatmentsSerializer
    # renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    # permission_classes = [ mmrdaPermissions , ]
    
    def post(self , request):
       
       
        try:
            if "contractor" in request.user.groups.values_list("name",flat=True):
                serializer = WasteTreatmentsSerializer(data = request.data , context={'request': request})
                if serializer.is_valid():
                    date = str(serializer.validated_data['dateOfMonitoring']).split('-')
                    month  = serializer.validated_data['month']
                    data = WasteTreatments.objects.filter(dateOfMonitoring__year = int(date[0]) , month = month ).exists()
                    if data == True:
                        return Response({'message':'already data filled for this Month'} , status=status.HTTP_400_BAD_REQUEST)
                    
                    else:
                        longitude = float(serializer.validated_data['waste_longitude'])
                        latitude = float(serializer.validated_data['waste_latitude'])
                        waste_location=Point(longitude,latitude,srid=4326)
                        
                        lat=float(serializer.validated_data['latitude'])
                        long=float(serializer.validated_data['longitude'])
                        location=Point(long,lat,srid=4326)
                        
                        waste_data =serializer.save(location=location , wasteHandlingLocation = waste_location , user = request.user)
                        data = wastetreatmentsViewserializer(waste_data).data
                        return Response({'status': 'success' , 
                                        'Message' : 'data saved successfully',
                                        'data' : data }, status = 200)
                else:
                    key, value =list(serializer.errors.items())[0]
                    error_message = key+" ," + value[0]
                    return Response({'status': 'error',
                                    'Message' :error_message} , status = status.HTTP_400_BAD_REQUEST)
            else:
                serializer = WasteTreatmentsSerializer(data = request.data , context={'request': request})
                if serializer.is_valid():
                    longitude = float(serializer.validated_data['waste_longitude'])
                    latitude = float(serializer.validated_data['waste_latitude'])
                    waste_location=Point(longitude,latitude,srid=4326)
                    
                    lat=float(serializer.validated_data['latitude'])
                    long=float(serializer.validated_data['longitude'])
                    location=Point(long,lat,srid=4326)

                    waste_data =serializer.save( location=location , wasteHandlingLocation = waste_location , user = request.user)
                    data = wastetreatmentsViewserializer(waste_data).data
                    return Response({'status': 'success' , 
                                        'Message' : 'data saved successfully',
                                        'data' : data }, status = 200)
                else:
                    key, value =list(serializer.errors.items())[0]
                    error_message = key+" ," + value[0]
                    return Response({'status': 'error',
                                    'Message' :error_message} , status = status.HTTP_400_BAD_REQUEST)
        except Exception:
            return  Response({'Message' : "Only consultant and Contractor can fill this form"}, status= status.HTTP_401_UNAUTHORIZED)


class wastemanagementUpdateView(generics.UpdateAPIView):
    serializer_class = wastetreatmentsViewserializer
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated, IsConsultant]
    
    def update(self, request , id , **kwargs):
        try:
            instance = WasteTreatments.objects.get(id=id,user=request.user.id)
        except Exception:
            return Response({"msg": "There is no Tree data for user %s" % (request.user.username)})
        serializer = WasteTreatmentsSerializer(instance , data=request.data , partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": "Please Enter a valid data"})

class MaterialSourcingView(generics.GenericAPIView):
    serializer_class = MaterialManagmentSerializer
    # renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    def post(self , request):
       
        
        try:
            if "contractor" in request.user.groups.values_list("name",flat=True):
                serializer = MaterialManagmentSerializer(data = request.data , context={'request': request})
                if serializer.is_valid():
                    date = str(serializer.validated_data['dateOfMonitoring']).split('-')
                    month  = serializer.validated_data['month']
                    data = MaterialManegmanet.objects.filter( dateOfMonitoring__year = int(date[0]) , month = month ).exists()
                    if data == True:
                        return Response({'message':'already data filled for this Month'} , status=status.HTTP_400_BAD_REQUEST)
                    else:
                        lat=float(serializer.validated_data['latitude'])
                        long=float(serializer.validated_data['longitude'])
                        location=Point(long,lat,srid=4326)

                        storagelong = float(serializer.validated_data['storageLongitude'])
                        storagelat = float(serializer.validated_data['storageLatitude'])
                        storageLocation = Point(storagelong , storagelat , srid = 4326 )

                        material_data =serializer.save(location=location , storageLocation = storageLocation , user = request.user)
                        data = MaterialSourcingViewserializer(material_data).data
                        return Response({'status': 'success' , 
                                        'Message' : 'data saved successfully',
                                        'data' : data }, status = 200)
                else:
                    key, value =list(serializer.errors.items())[0]
                    error_message = key+" ," + value[0]
                    return Response({'status': 'error',
                                    'Message' :value[0]} , status = status.HTTP_400_BAD_REQUEST)
            else:
                serializer = MaterialManagmentSerializer(data = request.data , context={'request': request})
                if serializer.is_valid(raise_exception = True):
                    material_data =serializer.save( location=location , storageLocation = storageLocation , user = request.user)
                    data = MaterialSourcingViewserializer(material_data).data
                    return Response({'status': 'success' , 
                                        'Message' : 'data saved successfully',
                                        'data' : data }, status = 200)
                else:
                    key, value =list(serializer.errors.items())[0]
                    error_message = key+" ," + value[0]
                    return Response({'status': 'error',
                                    'Message' :value[0]} , status = status.HTTP_400_BAD_REQUEST)
        except:
            return  Response({'Message' : "Only consultant and Contractor can fill this form"}, status= status.HTTP_401_UNAUTHORIZED)


class materialmanagemantUpdate(generics.UpdateAPIView):
    serializer_class = MaterialManagmentSerializer
    # renderer_classes = [ErrorRenderer]
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]
    
    def update(self, request , id , **kwargs):
        try:
            instance = MaterialManegmanet.objects.get(id=id,user=request.user.id)
        except Exception:
            return Response({"msg": "There is no Tree data for user %s" % (request.user.username)})
        serializer = MaterialManagmentSerializer(instance , data=request.data , partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"msg": "Please Enter a valid data"})


class TreemanagmentAPI(generics.GenericAPIView):
    serializer_class = TreemanagementSerializer
    def get(self, request,packages, *args, **kwargs):
            packages = packages
            instance = ExistingTreeManagment.objects.filter(packages__iexact=packages)
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
        instance = MaterialManegmanet.objects.filter(packages__iexact=packages)
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

