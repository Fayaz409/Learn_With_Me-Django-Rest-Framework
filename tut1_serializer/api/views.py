from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.

def student_detail(request,pk):
    student=Student.objects.get(id=pk)
    print('Students Queryset:',student)
    serializer=StudentSerializer(student)
    print('Serializer:',serializer)
    print('Serialiazer Data:',serializer.data)
    json_data=JSONRenderer().render(serializer.data)
    print('Json Data:',json_data)
    return HttpResponse(json_data,content_type='application/json')

def students_all_detail(request):
    students=Student.objects.all()
    print('Students Queryset:',students)
    serializer=StudentSerializer(students,many=True)
    print('Serializer:',serializer)
    print('Serialiazer Data:',serializer.data)
    json_data=JSONRenderer().render(serializer.data)
    print('Json Data:',json_data)
    return HttpResponse(json_data,content_type='application/json')
