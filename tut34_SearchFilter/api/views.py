from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name','city']
    # search_fields=['^name']

