from rest_framework import serializers
from .models import Player
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        
        extra_kwargs = {'passwords':{'write_only': True, 'required': True }}
    

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user