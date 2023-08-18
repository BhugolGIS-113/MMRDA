# Social Monitoring

Path : MMRDA/MMRDA/SocialMonitoring/views.py 

## Project Affected person (PAP) 

### PAP Post API

The `PapView` class is a view in a Django REST framework API that handles the creation of a PAP
(Project Affected person) object, with different validation and permission checks based on the user's group.



```python
#views.py
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


#serializer.py
class PapSerailzer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    longitude = serializers.CharField(max_length=50, required=True)
    latitude = serializers.CharField(max_length=50, required=True)
    class Meta:
        model = PAP
        fields = ('quarter', 'packages', 'longitude', 'latitude','dateOfMonitoring', 
                  'user','dateOfIdentification','PAPID','nameOfPAP', 
                  'addressLine1','streetName','pincode','eligibility', 'categoryOfPap', 
                    'areaOfAsset','typeOfStructure','legalStatus','legalDocuments',
                   'actionTaken', 'notAgreedReason','presentPhotograph','remarks' )

    def validate(self,data):
        long = data['longitude'].split('.')[-1]
        if len(long) > 6:
            raise serializers.ValidationError("longitude must have at most 6 digits after the decimal point.")
        lat =  data['latitude'].split('.')[-1]
        if len(lat) > 6:
            raise serializers.ValidationError("latitude must have at most 6 digits after the decimal point.")
        return data

    def create(self, data):
        data.pop('longitude')
        data.pop('latitude')
        return PAP.objects.create(**data)
    
```


### PAP Update API 

The `papupdateView` class is a view in a Django REST framework API that handles updating a PAP object with partial data.

```Python

#views.py
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


#serializer.py
class PapUpdateSerialzier(serializers.ModelSerializer):
    longitude = serializers.CharField(max_length=10, required=False)
    latitude = serializers.CharField(max_length=10, required=False)
    class Meta:
        model = PAP
        fields = ('quarter', 'packages', 'longitude', 'latitude', 'dateOfIdentification',
                  'addressLine1','streetName','pincode','eligibility', 'categoryOfPap',
                  'areaOfAsset','typeOfStructure','legalStatus','legalDocuments',
                   'actionTaken', 'notAgreedReason','presentPhotograph','remarks')
    def validate(self,data):
        long = data['longitude'].split('.')[-1]
        if len(long) > 6:
            raise serializers.ValidationError("longitude must have at most 6 digits after the decimal point.")
        lat =  data['latitude'].split('.')[-1]
        if len(lat) > 6:
            raise serializers.ValidationError("latitude must have at most 6 digits after the decimal point.")
        return data
```

### Post Rehabilitation API

The `RehabilitationView` class is a view in a Django REST framework API that handles the creation of rehabilitation data, with different validation and permission checks based on the user's group.

```python
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


#serializer.py
class RehabilitationSerializer(serializers.ModelSerializer):

    longitude = serializers.CharField(max_length=50, required=True  )
    latitude = serializers.CharField(max_length=50, required=True)
   

    class Meta:
        model = Rehabilitation
        fields = ('quarter','longitude', 'latitude','ID','dateOfRehabilitation' ,'PAPID', 'PAPName' ,'categoryOfPap','cashCompensation', 'compensationStatus',
                   'typeOfCompensation', 'otherCompensationType' ,'addressLine1','streetName','pincode',
                   'isShiftingAllowance','shiftingAllowanceAmount','isLivelihoodSupport', 'livelihoodSupportAmount','livelihoodSupportCondition',
                   'livelihoodSupportPhotograph','livelihoodSupportRemarks','isTraining','trainingCondition',
                   'trainingPhotograph' ,'trainingRemarks' , 'typeOfStructure'  ,'areaOfTenament' ,                       'tenamentsPhotograph',
                    'isRelocationAllowance' ,'RelocationAllowanceAmount' ,'isfinancialSupport',
                   'financialSupportAmount','isCommunityEngagement','isEngagementType', 'photographs' , 'documents','remarks')

    def validate(self,data):
        long = data['longitude'].split('.')[-1]
        if len(long) > 6:
            raise ValidationError("longitude must have at most 6 digits after the decimal point.")
        lat =  data['latitude'].split('.')[-1]
        if len(lat) > 6:
            raise ValidationError("latitude must have at most 6 digits after the decimal point.")
        return data

    def create(self, data):
        data.pop('longitude')
        data.pop('latitude')
        Rehabilitation_data = Rehabilitation.objects.create(**data)
  
        return Rehabilitation_data
```

### Post Labor Camp Details 
The below class is a view for creating and saving post-labour camp details with latitude and longitude coordinates.

```python

#views.py
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

#serializer.py
class labourCampDetailSerializer(serializers.ModelSerializer):
    longitude = serializers.CharField(max_length=10, required=False )
    latitude = serializers.CharField(max_length=8, required=False )
    class Meta:
        model = labourcampDetails
        fields = ('LabourCampName' , 'LabourCampId' , 'longitude' , 'latitude')

    def validate(self,data):
        long = data['longitude'].split('.')[-1]
        if len(long) > 6:
            raise serializers.ValidationError("longitude must have at most 6 digits after the decimal point.")
        lat =  data['latitude'].split('.')[-1]
        if len(lat) > 6:
            raise serializers.ValidationError("latitude must have at most 6 digits after the decimal point.")
        return data
    
    def create(self, data):
        data.pop('longitude')
        data.pop('latitude')
        return labourcampDetails.objects.create(**data) 


```


### Post Labor Camp Detail Form API

The `LabourCampDetailsView` class is a view in a Django REST framework API that allows authenticated
users who are either consultants or contractors to submit data for a labour camp, with different
validation and response logic based on the user's role.


```python

class LabourCampDetailsView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated & (IsConsultant | IsContractor)]
    parser_classes = [MultiPartParser]
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


#serializer.py
class LabourCampDetailSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    dateOfMonitoring = serializers.DateField(required=True)
    packages = serializers.CharField(validators=[MinLengthValidator(3)] , required=True)
    longitude = serializers.CharField(max_length=50, required=True)
    latitude = serializers.CharField(max_length=50, required=True)
    labourCampName = serializers.CharField(validators=[MinLengthValidator(3)] , required=True)
    labourCampId = serializers.CharField(validators=[MinLengthValidator(3)] , required=True)
    
    class Meta:
        model = LabourCamp
        fields = ('quarter', 'packages','dateOfMonitoring','longitude', 'latitude', 'labourCampName', 'labourCampId',
                  'isToilet', 'toiletCondition','toiletPhotograph','toiletRemarks',
                  'isDrinkingWater','drinkingWaterCondition' ,'drinkingWaterPhotographs','drinkingWaterRemarks',
                    'isDemarkationOfPathways','demarkationOfPathwaysCondition','demarkationOfPathwaysPhotographs','demarkationOfPathwaysRemark' ,
                    'isSignagesLabeling','signagesLabelingCondition' ,'signagesLabelingPhotographs','signagesLabelingRemarks',
                    'isKitchenArea','kitchenAreaCondition','kitchenAreaPhotographs','kitchenAreaRemarks',
                    'isFireExtinguish','fireExtinguishCondition','fireExtinguishPhotographs','fireExtinguishRemarks',
                     'isRoomsOrDoms' ,'roomsOrDomsCondition','roomsOrDomsPhotographs' ,'roomsOrDomsRemarks',
                     'isSegregationOfWaste','segregationOfWasteCondition','segregationOfWastePhotographs','segregationOfWasteRemarks',
                    'isRegularHealthCheckup','regularHealthCheckupCondition','regularHealthCheckupPhotographs','regularHealthCheckupRemarks',
                     'isAvailabilityOfDoctor', 'availabilityOfDoctorCondition','availabilityOfDoctorPhotographs','availabilityOfDoctorRemarks',
                      'isFirstAidKit','firstAidKitCondition' ,'firstAidKitPhotographs','firstAidKitRemarks',
                    'transportationFacility' ,'transportationFacilityCondition', 'modeOfTransportation','distanceFromSite',
                    'photographs' ,'documents','remarks')


    def validate(self,data):
        long = data['longitude'].split('.')[-1]
        if len(long) > 6:
            raise serializers.ValidationError("longitude must have at most 6 digits after the decimal point.")
        lat =  data['latitude'].split('.')[-1]
        if len(lat) > 6:
            raise serializers.ValidationError("latitude must have at most 6 digits after the decimal point.")
        

        return data
    
    def create(self,data):
        data.pop('longitude')
        data.pop('latitude')
        return LabourCamp.objects.create(**data)

```

### Update LaborCamp API

The `labourCampUpdateView` class is a view in a Django REST framework API that allows authenticated consultants to update labour camp data.

```python

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

#serializer.py
class LabourCampUpdateSerialzier(serializers.ModelSerializer):
    class Meta:
        model = LabourCamp
        fields = ('labourCampId' , 'labourCampName','isToilet','toiletCondition','toiletPhotograph','toiletRemarks',
                 'isDrinkingWater','drinkingWaterCondition' , 'drinkingWaterPhotographs', 'drinkingWaterRemarks',
                 'isDemarkationOfPathways','demarkationOfPathwaysCondition','demarkationOfPathwaysPhotographs' ,'demarkationOfPathwaysRemark',
                 'isSignagesLabeling','signagesLabelingPhotographs' ,'signagesLabelingRemarks' ,
                 'isKitchenArea','kitchenAreaCondition','kitchenAreaPhotographs','kitchenAreaRemarks',
                'isFireExtinguish','fireExtinguishCondition','fireExtinguishPhotographs','fireExtinguishRemarks',
                     'isRoomsOrDoms' ,'roomsOrDomsCondition','roomsOrDomsPhotographs' ,'roomsOrDomsRemarks',
                     'isSegregationOfWaste','segregationOfWasteCondition','segregationOfWastePhotographs','segregationOfWasteRemarks',
                    'isRegularHealthCheckup','regularHealthCheckupCondition','regularHealthCheckupPhotographs','regularHealthCheckupRemarks',
                     'isAvailabilityOfDoctor', 'availabilityOfDoctorCondition','availabilityOfDoctorPhotographs','availabilityOfDoctorRemarks',
                      'isFirstAidKit','firstAidKitCondition' ,'firstAidKitPhotographs','firstAidKitRemarks',
                    'transportationFacility' ,'transportationFacilityCondition', 'modeOfTransportation','distanceFromSite',
                    'photographs' ,'documents','remarks')

```

### Post constructionSite API

The `constructionSiteView` class is a view in a Django REST framework API that handles the creation of construction site data, with different validation and permission checks based on the user's role.


```python
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


#serialzier.py
class constructionSiteSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    quarter = serializers.CharField(validators=[MinLengthValidator(3)] , required=True)
    dateOfMonitoring = serializers.DateField(required=True)
    packages = serializers.CharField(validators=[MinLengthValidator(3)] , required=True)
    longitude = serializers.CharField(max_length=10, required=True)
    latitude = serializers.CharField(max_length=10, required=True)
    constructionSiteId = serializers.CharField(max_length = 255 , required = True)
    constructionSiteName = serializers.CharField(max_length = 255 , required = True)

    class Meta:
        model = ConstructionSiteDetails
        fields = ('quarter', 'packages','dateOfMonitoring' ,'longitude', 'latitude', 'constructionSiteName' , 'constructionSiteId',
                 'isDemarkationOfPathways','demarkationOfPathwaysCondition','demarkationOfPathwaysPhotographs','demarkationOfPathwaysRemark' ,
                'isSignagesLabelingCheck','signagesLabelingCondition' ,'signagesLabelingPhotographs','signagesLabelingRemarks',
                'isRegularHealthCheckup','regularHealthCheckupCondition','regularHealthCheckupPhotographs','regularHealthCheckupRemarks',
                  'isAvailabilityOfDoctor', 'availabilityOfDoctorCondition','availabilityOfDoctorPhotographs','availabilityOfDoctorRemarks',
                      'isFirstAidKit','firstAidKitCondition' ,'firstAidKitPhotographs','firstAidKitRemarks',
                   'isDrinkingWaterCheck','drinkingWaterCondition' ,'drinkingWaterPhotographs','drinkingWaterRemarks',
                    'isToilet', 'toiletCondition','toiletPhotograph','toiletRemarks',
                    'genralphotographs','documents','remarks')
    
    def validate(self,data):
        long = data['longitude'].split('.')[-1]
        if len(long) > 6:
            raise serializers.ValidationError("longitude must have at most 6 digits after the decimal point.")
        lat =  data['latitude'].split('.')[-1]
        if len(lat) > 6:
            raise serializers.ValidationError("latitude must have at most 6 digits after the decimal point.")
        return data

    def create(self,data):
        data.pop('longitude', None)
        data.pop('latitude', None)
        return ConstructionSiteDetails.objects.create(**data)
```


### Update ConstructionSite API

The ConstructionSiteUpdateView class is a view in a Python Django application that handles updating construction site data.

```python

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

```