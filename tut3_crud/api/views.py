from django.shortcuts import render
import io
from .models import Student
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def student_api(request):
    # student=Student.objects.all()
    # print('Students Queryset:',student)
    # return HttpResponse("Hello World")
    try:
        if request.method == 'GET':
            json_data = request.body
            print('Json Data:', json_data)
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id', None)
            if id is not None:
                try:
                    student = Student.objects.get(id=id)
                except Student.DoesNotExist:
                    return JsonResponse({'error': 'Student not found'}, status=404)
                serializer = StudentSerializer(student)
                json_data = JSONRenderer().render(serializer.data)
                print('Json Data with id:', json_data)
                return HttpResponse(json_data, content_type='application/json')
            
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        
        elif request.method=='POST':
            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            serializer=StudentSerializer(data=python_data)
            if serializer.is_valid():
                serializer.save()
                message={
                    'msg':'Data Inserted Successfully'
                
                }
                return HttpResponse(JSONRenderer().render(message),content_type='application/json')
            else:
                return HttpResponse(JSONRenderer().render(serializer.errors), content_type='application/json')
            
        elif request.method=='PUT':
            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            id=python_data.get('id')
            student=Student.objects.get(id=id)
            serializer=StudentSerializer(student,data=python_data,partial=True)
            if serializer.is_valid():
                serializer.save()
                message={
                    'msg':
                    'Your data has been updated successfully'
                }
                json_data=JSONRenderer().render(message)
                return HttpResponse(json_data,content_type='application/json')
            else:
                return HttpResponse(JSONRenderer().render(serializer.errors))
            
        elif request.method=='DELETE':
            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            id=python_data.get('id')
            student=Student.objects.get(id=id)
            student.delete()
            message={
                'msg':'Data has been removed Successfully'
            }
            # json_data=JSONRenderer().render(message)
            # return HttpResponse(json_data,content_type='application/json')
            return JsonResponse(message,safe=False)

                                




    
        
    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({'error': 'Something went wrong'}, status=500)

        