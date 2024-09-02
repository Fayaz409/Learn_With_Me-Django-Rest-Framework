from django.shortcuts import render
import io
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from api.serializers import StudentSerializer

@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)

            # Initialize the serializer with parsed data
            serializer = StudentSerializer(data=python_data)
            
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message': 'Data Inserted'}, status=201)  # HTTP 201 Created
            else:
                return JsonResponse(serializer.errors, status=400)  # HTTP 400 Bad Request
        except Exception as e:
            # Return a 500 Internal Server Error for any unexpected issues
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)  # HTTP 405 Method Not Allowed
