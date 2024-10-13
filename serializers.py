# api/serializers.py
from rest_framework import serializers
from .models import User, Complaint

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'
