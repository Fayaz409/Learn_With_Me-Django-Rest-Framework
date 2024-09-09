from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
# Create your views here.

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[SearchFilter]
    filterset_fields=['name','city']


