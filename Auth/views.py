from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import Group
from Auth.models import User 
from .serializers import (
    LoginSerializer, RegisterSerializer , LogoutSerializer , ChangePasswordSerializer ,
    PasswordRestSerializer,PasswordResetEmailSerializer)
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from .renderers import ErrorRenderer
from rest_framework.parsers import MultiPartParser
import json
from rest_framework import status
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken , BlacklistedToken
from django.contrib.auth import authenticate



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



# The `UserRegister` class is a view that handles user registration and assigns the user to a specific
# group based on their selected options.
class UserRegister(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    ErrorRenderer = [ErrorRenderer]
    parser_classes = [MultiPartParser]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                mmrda_group = Group.objects.get(name='mmrda')
                kfw_group = Group.objects.get(name="kfw")
                consultant_group = Group.objects.get(name='consultant')
                contractor_group = Group.objects.get(name='contractor')
                RNR_group = Group.objects.get(name = 'RNR')
                if user.is_mmrda:
                    user.groups.add(mmrda_group)

                elif user.is_kfw == True:
                    user.groups.add(kfw_group)

                elif user.is_consultant == True:
                    user.groups.add(consultant_group)

                elif user.is_contractor == True:
                    user.groups.add(contractor_group)

                elif user.is_RNR == True:
                    user.groups.add(RNR_group)

                return Response({'msg': 'Registration Successfull' }, status=200)
            except:
                return Response({'msg': 'Please select any one group'}, status=400)
        else:
            return Response({'msg': 'Registration NotSuccessfull'}, status=400)


# class LoginView(generics.GenericAPIView):
#     serializer_class = LoginSerializer
#     renderer_classes = [ErrorRenderer]
#     parser_classes = [MultiPartParser]


#     def post(self, request):
     
#             serializer = LoginSerializer(data=request.data)
#             if serializer.is_valid(raise_exception=True):
#                 user_data = serializer.validated_data
#                 # user = RegisterSerializer(user_data).data
#                 if serializer is not None:
#                     token = get_tokens_for_user(serializer.validated_data)
#                     return Response({'Token': token, 'msg': 'Login sucessfull',
#                                     'status': 200,
#                                     'user_id': user_data.id , 'user': user_data.email,
#                                     'username' :user_data.username,
#                                     'user_group': user_data.groups.values_list("name", flat=True)[0]},
#                                     status=200)
#             else:
#                 return Response({'msg': serializer.errors,
#                             'status': 400,
#                             'response': 'Bad Request'}, status=400)

        # except:
        #     return Response({'msg': "Something Went Wromg Pelase Try Again in Sometime",
        #                     'status': 400,
        #                     'response': 'Bad Request'}, status=400)


# # "user_group": user_data.groups.values_list("name", flat=True)'group
# print(request.user.groups.all())
# print(json.dumps(user_data.groups.values_list("name",flat=True)))
# user["user_group"]=user_data.groups.values_list("name",flat=True)[0]




# The above class is a login view in Python that handles user authentication and returns a response
# with a token and user information if the login is successful.
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    parser_classes = [MultiPartParser]

    def post(self , request):
        serializer = LoginSerializer(data= request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email , password=password)
            user1 = User.objects.filter(email=email)
            serializer2 = RegisterSerializer(user1 ,many=True)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'Token':token,
                                'status': 'success',
                                'Message':'Login sucessfull', 
                                "user": serializer2.data[0].get('email'),
                                "username": serializer2.data[0].get('username'),
                                'user_group' : user.groups.values_list("name",flat=True)[0]} , 
                                status=status.HTTP_200_OK)
        else:
            return Response({'status': 'failed',
                            'Message': "Email OR Password is not Valid , Please check Again."} , status=status.HTTP_404_NOT_FOUND)





# The `ChangePasswordView` class is a view in a Python Django application that handles the logic for
# changing a user's password.
class ChangePasswordView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    parser_classes = [MultiPartParser]
    
    def post(self, request , format = None):
      serializer = ChangePasswordSerializer(data=request.data , context ={'user':request.user})
      serializer.is_valid(raise_exception=True)
      return Response({'msg':'password change successfully',
                        'status' : 201}, status=status.HTTP_201_CREATED)

# The above class is a view for handling password reset email requests in a Django REST framework API.
class PasswordRestEmail(generics.GenericAPIView):
    serializer_class = PasswordResetEmailSerializer
    parser_classes = [MultiPartParser]
    def post (self , request):
        serializer = PasswordResetEmailSerializer(data = request.data)
       
        serializer.is_valid(raise_exception=True)
        print(serializer.data)
        return Response({'message':'Password Rest Email sent Successfully' } , status= status.HTTP_200_OK)


# The `restpasswordView` class is a generic API view in Python that handles password reset requests
# and returns a response indicating whether the password reset was successful or not.
class restpasswordView(generics.GenericAPIView):
    serializer_class = PasswordRestSerializer
    parser_classes = [MultiPartParser]
    def post(self , request ,uid, token ):
        serializer = PasswordRestSerializer(data = request.data , context = {'uid' :uid ,'token' :token })
        serializer.is_valid(raise_exception=True)
        return Response({"message" : "Password reset Successfully"} , status=status.HTTP_200_OK)

# The `LogoutAPIView` class is a view that handles user logout by validating the request data, saving
# the serializer, and returning a response indicating successful logout.

class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer 
    parser_classes = [MultiPartParser]

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # token = OutstandingToken.objects.filter(user_id = userid).delete()
        # print('Outstanding token deleted successfully')
  

        return Response({'message' : 'Logut Successfull'}, status=status.HTTP_204_NO_CONTENT)