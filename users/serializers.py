from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', 'username', 'email', 'university', 'status', 'academic_year')

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name', 'username', 'email', 'password', 'university', 'status', 'academic_year')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            full_name=validated_data['full_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            university=validated_data['university'],
            status=validated_data['status'],
            academic_year=validated_data['academic_year'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name', 'email', 'university', 'status', 'academic_year')
        extra_kwargs = {'email': {'required': True}}
