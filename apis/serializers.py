from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt import serializers as jwt_serial
from .models import (UserInfo,)

class TokenObtainPairSerializer(jwt_serial.TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super(TokenObtainPairSerializer, self).validate(attrs)
        refresh = self.get_token(self.user)
        data.update(refresh.payload)
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('user', 'client_id', 'client_secret_key')

    def validate_client_id(self, value):
        if not value.startswith('pradam'):
            raise serializers.ValidationError('Client ID should starts with Pradam')
        return value
