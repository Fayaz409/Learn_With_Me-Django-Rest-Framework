from django.shortcuts import render
from .models import Student
from rest_framework.generics import ListAPIView
from .serializers import StudentSerializer
from rest_framework.pagination import PageNumberPagination
from .mypaginations import MyPagination
# Create your views here.

class StudentAPI(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=MyPagination

