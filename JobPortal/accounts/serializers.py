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
    
