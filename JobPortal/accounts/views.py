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