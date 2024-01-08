from rest_framework import serializers
from .models import User, Freelancer, Client
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import check_password
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response




class ClientRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 68, min_length = 6, write_only = True)
    password2 = serializers.CharField(max_length = 68, min_length = 6, write_only = True)
    class Meta:
        model = User
        fields = ['email','first_name','last_name','password','password2',]

    def validate(self, attrs):
        password = attrs.get('password', '')
        password2 = attrs.get('password2', '')
        if password != password2:
            raise serializers.ValidationError({'message':' password dosent match'})
            
        return attrs
    
    def create(self, validated_data):

        validated_data['is_client'] = True


        # Create a new user
        user = User.objects.create_user(
            email = validated_data['email'],
            first_name = validated_data.get('first_name'),
            last_name = validated_data.get('last_name'),
            password = validated_data.get('password'),
            is_client = True
        )

        if validated_data['is_client']:
            client_data = {'user': user}
            client = Client.objects.create(**client_data)


        return user





class FreelancerRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 68, min_length = 6, write_only = True)
    password2 = serializers.CharField(max_length = 68, min_length = 6, write_only = True)
    class Meta:
        model = User
        fields = ['email','first_name','last_name','password','password2']

    def validate(self, attrs):
        password = attrs.get('password', '')
        password2 = attrs.get('password2', '')
        if password != password2:
            raise serializers.ValidationError({'message':' password dosent match'})
            
        return attrs
    
    def create(self, validated_data):
        validated_data['is_freelancer'] = True


        # Create a new user
        user = User.objects.create_user(

            email=validated_data['email'],
            first_name = validated_data.get('first_name'),
            last_name = validated_data.get('last_name'),
            password=validated_data.get('password'),
            is_freelancer = True 
        )

        if validated_data['is_freelancer']:
            # If the user is a freelancer, create a freelance profile
            freelancer_data = {'user': user}
            freelancer = Freelancer.objects.create(**freelancer_data)



        return user

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255, min_length = 6)
    password = serializers.CharField(max_length = 68, write_only = True)
    full_name = serializers.CharField(max_length = 255, read_only = True)
    access_token = serializers.CharField(max_length = 255, read_only = True)
    refresh_token = serializers.CharField(max_length = 255, read_only = True)
    user_type = serializers.CharField(max_length=20, read_only=True)
    
    class Meta:
        model = User
        fields = ['email','password','full_name','access_token','refresh_token','user_type']
        
        
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        request = self.context.get('request')
        user = authenticate(request, email = email, password = password)
        
        
        if user is None:
            raise AuthenticationFailed('Invalid email or passsword!')
        
        user_type = None
        
        if  hasattr(user, 'client'):
            user_type = 'client'
        elif  hasattr(user, 'freelancer'):
            user_type = 'freelancer'
        else:
            raise AuthenticationFailed('User does not have client or freelancer credentials.')
        
        

        
        
        user_tokens = user.tokens()
            
        attrs['full_name'] = user.get_full_name()
        attrs['access_token'] = user_tokens.get('access')
        attrs['refresh_token'] = user_tokens.get('refresh')
        attrs['user_type'] = user_type
        
        return attrs


class FreelancerLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255, min_length = 6)
    password = serializers.CharField(max_length = 68, write_only = True)
    full_name = serializers.CharField(max_length = 255, read_only = True)
    access_token = serializers.CharField(max_length = 255, read_only = True)
    refresh_token = serializers.CharField(max_length = 255, read_only = True)
    user_type = serializers.CharField(max_length=20, read_only=True)
    
    class Meta:
        model = User
        fields = ['email','password','full_name','access_token','refresh_token','user_type']
        
        
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        request = self.context.get('request')
        user = authenticate(request, email = email, password = password)

        if not user or not hasattr(user, 'freelancer'):
            raise AuthenticationFailed('Invalid credentials. Please try again.')
        
        user_tokens = user.tokens()
            
        return {
            'email' : user.email,
            'full_name' : user.get_full_name,
            'access_token' : user_tokens.get('access'),
            'refresh_token' : user_tokens.get('refresh'),
            'user_type': 'freelancer',

        }
        
        
class ClientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['user', 'profilepic', 'phone', 'address', 'about']
        
    def validate(self, attrs):
        method = self.context['request'].method  # Get the HTTP method used
        if method == 'POST':
            # Validate all fields when method is POST
            required_fields = ['profilepic', 'phone', 'address', 'about']
            for field in required_fields:
                if attrs.get(field) is None:
                    raise serializers.ValidationError(f"{field} is required for POST requests.")
        return attrs

    def create(self, validated_data):
        return Client.objects.create(**validated_data)
        
        