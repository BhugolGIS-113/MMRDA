from rest_framework import serializers
from .models import (User  ,)
from django.contrib.auth import authenticate
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework_simplejwt.tokens import RefreshToken, TokenError , AccessToken
from django.utils.http import urlsafe_base64_decode , urlsafe_base64_encode
from django.utils.encoding import smart_str , force_bytes , DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .utils import *
from xml.dom import ValidationErr

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style = {'input_type':'password'},write_only = True)
    class Meta:
        model = User
        fields = ('email','username' ,  'password','is_mmrda' , 'is_kfw' , 'is_contractor' , 'is_consultant')


    def create(self,validated_data):
        return User.objects.create_user(**validated_data)



class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ("email", "password")

        extra_kwargs ={'password':{'write_only':True}}


    def validate(self,data):
       return authenticate(**data)
       
class ChangePasswordSerializer(serializers.Serializer):
   password = serializers.CharField(max_length=255 , style={'input_type':'password'}, write_only =True)
#    password2 = serializers.CharField(max_length=255 , style={'input_type':'password'}, write_only =True)
   class Meta:
    Feilds = ["password"]
   
   def validate(self, data):
    password = data.get('password')
    user = self.context.get('user')
    # if password:
    #     raise serializers.ValidationError("password and confirm password doesn't match")
    user.set_password(password)
    user.save()
    return data


class PasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.CharField(max_length = 255)
    class Meta:
        fileds = ['email']


    def validate(self, data):
        email = data.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print("Encoded ID" , uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print("Password reset Token" , token)
            link = 'http://localhost:3000/api/auth/reset/'+ uid+'/'+token
            print("password Rest link" , link)
            
            body = 'click following link to reset your Password : ' + link  
            data = {
                'subject' : 'Reset Your Password ',
                'body' : body,
                'to_email':user.email
            }
            Util.send_email(data)

        else:
            raise ValidationErr("You are not a registered user")
        return data

class PasswordRestSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255 , style={'input_type':'password'}, write_only =True)
    class Meta:
        Feilds = ["password"]
   
    def validate(self, data):
        try:
            password = data.get('password')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if data["password"] == "" or data["password"] == None:
                raise serializers.ValidationError("password cannot be empty")
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id =id)
            if not PasswordResetTokenGenerator().check_token(user , token):
                raise ValidationErr("Token is not Valid or Expired")
            user.set_password(password)
            user.save()
            return data
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user , token)
            raise ValidationErr("Token is not Valid or Expired")




class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid'),
    }
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        
        except TokenError:
            self.fail('bad_token')

        


        

