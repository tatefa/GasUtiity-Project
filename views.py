from django.shortcuts import render

# Create your views here.
# api/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User, Complaint
from .serializers import UserSerializer, ComplaintSerializer
from django.contrib.auth.hashers import make_password

class UserViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(password=make_password(request.data['password']))  # Hash the password
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ComplaintViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            # Generate a unique ticket ID
            serializer.validated_data['ticket_id'] = str(Complaint.objects.count() + 1)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        complaints = Complaint.objects.all()
        serializer = ComplaintSerializer(complaints, many=True)
        return Response(serializer.data)
