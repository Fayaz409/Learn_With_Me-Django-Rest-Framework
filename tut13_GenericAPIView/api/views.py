from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from .serializers import StudentSerializer
# Create your views here.



class StudentList(GenericAPIView,ListModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
class StudentCreate(CreateModelMixin,GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class StudentRetrieve(RetrieveModelMixin,GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class StudentUpdate(UpdateModelMixin,GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
class StudentDelete(DestroyModelMixin,GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)















# class StudentAPI(APIView):

#     def get(slef,request,pk=None,format=None):
#         if pk is not None:
#             student = Student.objects.get(id=pk)
#             serializer = StudentSerializer(student)
#             return Response(serializer.data)
#         students = Student.objects.all()
#         serializer = StudentSerializer(students,many=True)
#         return Response(serializer.data)
    
#     def post(self,request,format=None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created'})
#         else:
#             return Response(serializer.errors)
        
#     def put(self,request,pk,format=None):
#         student = Student.objects.get(id=pk)
#         serializer = StudentSerializer(student,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Updated Successfully'})
#         return Response(serializer.errors)
    
#     def patch(self,request,pk,format=None):
#         student = Student.objects.get(id=pk)
#         serializer = StudentSerializer(student,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial Update: Data Updated Successfully'})
#         return Response(serializer.error)
    
#     def delete(self,request,pk,format=None):
#         student=Student.objects.get(id=pk)
#         if student:
#             student.delete()
#             return Response({'msg':'Student Deleted Successfully! '})
#         return Response({'msg':'Data Does Not Exist'})
    

