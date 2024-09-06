from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET','POST','PATCH','PUT','DELETE'])
def student_api(request,pk=None):


    if request.method=='GET':
        id=pk
        if id is not None:
            student=Student.objects.get(id=id)
            serializer=StudentSerializer(student)
            return Response(serializer.data)
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res={
                'msg':'Student Created Successfully'
            }
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method=='PUT':
        id=pk
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            res={
                'msg':'Complete Updated Successfully'
            }
            return Response(res,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method=='PATCH':
        id=pk
        student=Student.objects.get(id=pk)
        serializer=StudentSerializer(student,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={
                'msg':' Partial Data Updated Successfully'
            }
            return Response(res)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)





    elif request.method=='DELETE':
        id=pk
        student=Student.objects.get(id=id)
        # serializer=StudentSerializer(student)
        if student:
            student.delete()
            res={
                'msg':'Student Deleted Successfully'
            }
            return Response(res)
        return Response({'msg':'User Does not Exist'})
     

