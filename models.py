# api/models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  # Store hashed password

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complaint_type = models.CharField(max_length=50)
    description = models.TextField()
    ticket_id = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=20, default='Pending')
