from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .customepermissions import MyPermission
from rest_framework.authentication import TokenAuthentication
from api.customauth import CustomAuthentication
# Create your views here.

class StudentAPI(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[CustomAuthentication]
    permission_classes=[IsAuthenticated]