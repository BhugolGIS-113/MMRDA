
from rest_framework import serializers
from .models import traning , photographs

class TraningSerializer(serializers.ModelSerializer):
    class Meta:
        model = traning
        fields = '__all__'


class photographsSerializer(serializers.ModelSerializer):
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    class Meta:
        model = photographs
        fields = ['photograph_title', 'photographs_uploaded_by' , 'longitude' , 'latitude',
                   'date' , 'site_photographs'  ]

    def create(self,data):
        data.pop('latitude')
        data.pop('longitude')
        return photographs.objects.create(**data)

class photographsViewSerializer(serializers.ModelSerializer):
    longitude=serializers.CharField(max_length=10,required=False)
    latitude=serializers.CharField(max_length=10,required=False)
    class Meta:
        model = photographs
        fields =['id','photograph_title', 'photographs_uploaded_by' , 'longitude' , 'latitude',
                   'date' , 'site_photographs'  ]