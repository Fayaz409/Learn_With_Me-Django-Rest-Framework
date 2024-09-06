from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Student
from .serializers import StudentSerializer
# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def student_api(request):
    if request.method=='GET':
        id=request.data.get('id')
        if id is not None:
             student=Student.objects.get(id=id)
             serializer=StudentSerializer(student)
             return Response(serializer.data,content_type='application/json')
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        print(request.data)
        data=request.data
        serializer=StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            message={
                'msg':'Your Data is Stored'
            }
            return Response(message)
        return Response(serializer.errors)
        # return Response({'msg':'This is post Request with Data:{request.body}'})
    elif request.method=='PUT':
        id=request.data.get('id')
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={
                'msg':'Your data had been updated'
            }
            return Response(res)
        return Response(serializer.errors)
    
    elif request.method=='DELETE':
        id=request.data.get('id')
        student=Student.objects.get(id=id)
        if student:
            student.delete()
            message={

                'msg':'Data Deleted Successfully'
            }
            return Response(message)
    return Response({'msg':'Data does not exist'})



