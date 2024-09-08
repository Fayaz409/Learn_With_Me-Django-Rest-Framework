from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from .serializers import StudentSerializer
from .models import Student
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET','PUT','DELETE','POST','PATCH'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request,pk=None):

    if request.method=='GET':
        id=pk
        if id is not None:
            student=Student.objects.get(id=id)
            serializer=StudentSerializer(student)
            return Response(serializer.data)
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res={
                'msg':'Student Created Successfully'
            }
            return Response(res)
        return Response(serializer.eerors)
    
    elif request.method=='PUT':
        student=Student.objects.get(id=pk)
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            res={
                'msg':'Data Updated Successfully!'
            }
            return Response(res)
        return Response(serializer.errors)
    
    elif request.method=='PATCH':
        student=Student.objects.get(id=pk)
        serializer=StudentSerializer(student,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={
                'msg':'Partial Data Updated'
            }
            return Response(res)
        return Response(serializer.errors)
    
    elif request.method=='DELETE':
        student=Student.objects.get(id=pk)
        if student:
            student.delete()
            res={
                'msg':'Student Deleted Successfully:'
            }
            return Response(res)
        return Response({'msg':'User Does Not Exist'})
    


    
    

