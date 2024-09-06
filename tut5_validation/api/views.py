from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):
    def get(self,request,*args,**kwargs):
        # if request.method=="GET":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id',None)                                               
        if id is not None:
            student=Student.objects.get(id=id)
            serializer=StudentSerializer(student)
            # json_data=JSONRenderer().render(serializer.data)
            return JsonResponse(serializer.data,safe=False)
        student=Student.objects.all()
        serializer=StudentSerializer(student,many=True)
        # json_data=JSONRenderer().render(serializer.data)
        return JsonResponse(serializer.data,safe=False)
    def post(self,request,*args,**kwargs):
        # if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            message={
                'msg':'Your data is created Successfully'
            }
            return JsonResponse(message,content_type='application/json')
        return JsonResponse(serializer.errors,safe=False)
    def delete(self,request,*args,**kwargs):
        # if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        student=Student.objects.get(id=id)
        student.delete()
        message={
            'msg':"Data deleted Successfully"        }
        return JsonResponse(message,content_type='application/json')
    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            message={
                'msg':'Your data is updated Successfully'
            }
            return JsonResponse(message,content_type='application/json')
        return JsonResponse(serializer.errors,safe=False)
            






# def student_api(request):
#     if request.method=="GET":
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         id=python_data.get('id',None)                                               
#         if id is not None:
#             student=Student.objects.get(id=id)
#             serializer=StudentSerializer(student)
#             json_data=JSONRenderer().render(serializer.data)
#             return JsonResponse(json_data,safe=False)
#         student=Student.objects.all()
#         serializer=StudentSerializer(student,many=True)
#         # json_data=JSONRenderer().render(serializer.data)
#         return JsonResponse(serializer.data,safe=False)
#     if request.method=="POST":
#         json_data=request.body()
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         serializer=StudentSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             message={
#                 'msg':'Data Created'
#             }
#             return JsonResponse(message,content_type='application/json')
#         return JsonResponse(serializer.errors,safe=False)
#     if request.method=='PUT':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         id=python_data.get('id')
#         student=Student.objects.get(id=id)
#         serializer=StudentSerializer(student,data=python_data)
#         if serializer.is_valid():
#             serializer.svae()
#             message={
#                 'msg':'Your data is updated'
#             }
#             return JsonResponse(message,content_type='application/json')
#         return JsonResponse(serializer.errors,safe=False)
#     if request.method=='DELETE':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         id=python_data.get(id=id)
#         student=Student.objects.get(id=id)
#         student.delete()
#         message={
#             'msg':"Data deleted Successfully"        }
#         return JsonResponse(message,content_type='application/json')

        