from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import *
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return{
        
        'refresh': str(refresh),
        'access': str(refresh.access_token),    
    }
    
class Register(APIView):
    def get(self, request):
        return Response({"Message" : "PLEASE REGISTER YOURSELF"})
    
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save(); token = get_tokens_for_user(user)
            return Response(
                {
                    "token" : token,
                    "Message" : "REGISTRATION SUCCESSFUL"
                },
                status = status.HTTP_200_OK
                )
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

class Login(APIView):
    def get(self, request):
        return Response({"Message" : "PLEASE LOGIN"})
    
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email = email, password = password)
            if user:
                token = get_tokens_for_user(user)
                return Response(
                    {
                        "token" : token,
                        "MESSAGE" : "LOGIN SUCCESSFUL"
                    },
                    status = status.HTTP_200_OK
                )
            return Response(
                {
                    "ERROR" : "INVALID USER"
                }
            )
            
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    
class Profile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = ProfileSerializer(request.user)
        print("PROFILE VIEW ---------->", request.user.profile, request.user)
        return Response (serializer.data, status = status.HTTP_200_OK)  
    
    def post(self, request):
        serializer = ProfileSerializer(request.user.profile, data = request.data)
        print("PROFILE IMAGE DATA ---------->", request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(
                 {
                     "Message" : "Profile Updated Successfully"
                 },
                 status = status.HTTP_200_OK
             )
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)