from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets 
# Create your views here.


class StudentViewSet(viewsets.ViewSet):

    def list(self,request):
        student=Student.objects.all()
        serializer=StudentSerializer(student,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            student=Student.objects.get(id=id)
            serializer=StudentSerializer(student)
            return Response(serializer.data)
        
    def create(self,request):
        serializer=StudentSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created Successfully'})
        return Response(serializer.errors)
    
    def update(self,request,pk):
        student=Student.objects.get(id=pk)
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated Successfully'})
        return Response(serializer.errors)
    
    def partial_update(self,request,pk):
        student=Student.objects.get(id=pk)
        serializer=StudentSerializer(student,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        
    def delete(self,request,pk):
        student=Student.objects.get(id=pk)
        if student:
            student.delete()
            return Response({'msg':'Data Deleted Successfully'})
        return Response({'msg':' This Student Does not Exist! '})
    
    
