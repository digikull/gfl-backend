from rest_framework import serializers
from .models import OTPVerifiaction

class OTPVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTPVerifiaction
        fields = '__all__'