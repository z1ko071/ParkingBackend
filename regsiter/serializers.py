from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate


# class RegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['email', 'password', 'fullname', 'date_of_birth', 'image', 'car_number']
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         user = CustomUser.objects.create_user(**validated_data)
#         return user


# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(style={'input_type': 'password'})


# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField()
#
#     def validate(self, data):
#         email = data.get('email')
#         print(email)
#         password = data.get('password')
#         print(password)
#
#         if email and password:
#             user = authenticate(request=self.context.get('request'),
#                                 email=email, password=password)
#             print(f'{user}')
#             if user is None:
#                 raise serializers.ValidationError("Invalid email/password. Please try again.")
#
#             if not user.is_active:
#                 raise serializers.ValidationError("User is deactivated.")
#
#         else:
#             raise serializers.ValidationError('Must include "email" and "password".')
#
#         data['user'] = user
#         return data

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'full_name', 'date_of_birth', 'image', 'car_number']


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'date_of_birth', 'image', 'car_number']
