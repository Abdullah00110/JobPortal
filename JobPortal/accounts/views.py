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
    
class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={"user" : request.user} )
        if serializer.is_valid():
            return Response(
                {
                    "Message" : "Password Changed Successfully"
                },
                status = status.HTTP_200_OK
            )
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class PasswordResetEmail(APIView) :
    def post(self, request) :
        serializer = PasswordResetEmailSerializer(data=request.data)
        if serializer.is_valid() :
            return Response(
                                {
                                    "Message" : "Password reset link send to your email. Please check your email"
                                }, 
                                status=status.HTTP_200_OK
                            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ResetPassword(APIView) :
    def post(self, request, uid, token) :
        serializer = PasswordResetSerializer(data=request.data, context={"uid" : uid, "token" : token})
        if serializer.is_valid() :
            return Response(
                                {
                                    "Message" : "Password Reset Successfully"
                                }, 
                                status=status.HTTP_200_OK
                            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddEducation(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        education = Education.objects.filter(user = request.user)
        serializer = EducationSerializer(education, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    def post(self, request):
        serializer = EducationSerializer(data = request.data, context = {"user" : request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "Message" : "Education details added successfully"
                },
                status = status.HTTP_200_OK
            )
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    
class AddSkill(APIView) :
    permission_classes = [IsAuthenticated]
    def get(self, request) :
        return Response({"MESSAGE" : "ADD YOUR SKILLS HERE"}, status=status.HTTP_200_OK)

    def post(self, request) :
        skill = request.data.get("skill").upper()
        skill = Skills.objects.get_or_create(skill=skill)[0]
        userskill = UserSkills.objects.get_or_create(user=request.user, skill=skill)[0]
        serializer = SkillSerializer(userskill)
        return Response(
                            {"MESSAGE" : "EDUCATION DETAILS ADDED SUCCESSFULLY", "DATA" : serializer.data},
                            status=status.HTTP_200_OK
                        )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AddProject(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ProjectSerializer(data=request.data, context={"user": request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "MESSAGE" : "PROJECT DETAILS ADDED SUCCESSFULLY"
                }
                status = status.HTTP_200_OK
            )
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class AddExperience(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ExperienceSerializer(data=request.data, context={"user" : request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "MESSAGE" : "EXPERIENCE DETAILS ADDED SUCCESSFULLY"
                },
                status = status.HTTP_200_OK
            )
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    