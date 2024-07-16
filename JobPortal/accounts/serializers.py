from rest_framework import serializers
from accounts.models import *
from django.utils.encoding import smart_str
from django.utils.encoding import force_bytes
from django.utils.encoding import DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from xml.dom import ValidationErr


class RegisterSerializer(serializers.ModelSerializer) :
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, style={"input_type" : "password"})
    class Meta :
        model = User
        fields = ["email", "name", "password", "password2", "tc"]

    def validate(self, attrs) :
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2 :
            raise serializers.ValidationError("Password doesn't match")
        return attrs

    def create(self, validated_data) :
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 300)
    class Meta:
        model = User
        fields = ["email", "password"]
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "image"]
    def update(self, instance, validated_data):
        print("\n\nPROFILE IMAGE STARTED ---------->\n", instance, "-", instance.image, "-", validated_data)
        instance.image = validated_data.get("image", instance.image)
        instance.save()
        return instance
    
class ChangePasswordSerializer(serializers.Serializer) :
    password = serializers.CharField(max_length = 300, style = {"input_type" : "password"}, write_only = True)
    password2 = serializers.CharField(max_length = 300, style = {"input_type" : "password"}, write_only = True)

    class Meta :
        fields = ["password", "password2"]

    def validate(self, attrs) :
        password = attrs.get("password")
        password2 = attrs.get("password2")
        user = self.context.get("user")
        old_password = user.password
        if password != password2 :
            raise serializers.ValidationError("Both password should match")
        if user.check_password(password) :
            raise serializers.ValidationError("New Password Should not match to the current Password")
        user.set_password(password)
        user.save()
        return attrs
    
class PasswordResetEmailSerializer(serializers.Serializer) :
    email = serializers.EmailField(max_length = 300)
    class Meta :
        fields = ["email"]

    def validate(self, attrs) :
        email = attrs.get("email")
        if User.objects.filter(email = email).exists() :
            user = User.objects.get(email = email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            link = "http://127.0.0.1:8000/jobportal/accounts/reset-password/" + uid + "/" + token
            print("\n\nLINKE SENDED --->", link, "\n\n")
            data = {
                        "subject" : "Reset Your Password",
                        "body" : "CLICK here to reset your password",
                        "to_email" : user.email
                    }
            return attrs
        raise ValidationErr("You are NOT a registered user")
    
class PasswordResetSerializer(serializers.Serializer) :
    password = serializers.CharField(max_length = 300, style = {"input_type" : "password"}, write_only = True)
    password2 = serializers.CharField(max_length = 300, style = {"input_type" : "password"}, write_only = True)

    class Meta :
        fields = ["password", "password2"]

    def validate(self, attrs) :
        try :
            password = attrs.get("password")
            password2 = attrs.get("password2")
            uid = self.context.get("uid")
            token = self.context.get("token")
            if password != password2 :
                raise serializers.ValidationError("Both password should match")
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id = id)
            if not PasswordResetTokenGenerator().check_token(user, token) :
                raise ValidationError("Token is NOT valid or it may be EXPIRED")
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier :
            PasswordResetTokenGenerator().check_token(user, token)
            raise ValidationError("Token is Invalid or EXPIRED")

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['degree', 'specialization', 'institution', 'board_or_university', 'passing_year']
        
    def create(self, validated_data):
        user = self.context.get("user")
        education = Education.objects.create(user = user, **validated_data)
        return education

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSkills
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "title", "role", "description"]
        
    def create(self, validated_data):
        user = self.context.get("user")
        project = Project.objects.create(user=user, **validated_data)
        return project
    
class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ["id", "job_role", "experience_year", "company", "start_date", "end_date"]
    def create(self, validated_data):
        user = self.context.get("user")
        experience = Experience.objects.create(user=user, **validated_data)
        return experience